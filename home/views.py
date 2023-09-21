from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import scipy.stats
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, PatternFill, Font
import math
import random




def home(request):
    return render(request,'home.html')



def simulation(request):
    if request.method == 'POST':
        # Retrieve user-provided Python code from POST request
        simulation_period = request.POST.get('sim_process_file_code')
        months = request.POST.get('months')
        sim_process_row_code = request.POST.get('sim_process_row_code')
        sim_save_output_code = request.POST.get('sim_save_output_code')
        cb = request.POST.get('cb')  # Checkbox value for "Remove Negative"
        cb1 = request.POST.get('cb1')  # Checkbox value for "Round Lead Time"
        browse = request.FILES.get('filedata')

        print("cccccccccccccccccccccccccccccsimuolation",simulation_period)

        # Load data (replace this with your data source)
        df = pd.read_excel('your_data.xlsx')

        simulation_time = 12  # Change this to your desired simulation time

        df['Prev_Order'] = pd.NA

        def sim_process_row(row, ci, simulation_duration_type):
            if pd.isna(row['ItemNumber']):
                return row

            if ci == 1:
                cs = row['Current Stock']
                prev_stock = 0 if pd.isna(cs) else cs
            else:
                prev_stock = row[simulation_duration_type + str(ci - 1)]

            current_index = simulation_duration_type + str(ci)
            deviation = 0.1  # Modify this as needed

            if simulation_duration_type == 'M':
                if float(deviation) == float(0):
                    average_consumption = 0.00 if pd.isna(row['Avrg. Consumption/Mnth']) else float(
                        row['Avrg. Consumption/Mnth'])
                else:
                    average_consumption = 0.00 if pd.isna(row['Avrg. Consumption/Mnth']) else float(
                        row['Avrg. Consumption/Mnth'])
                    limit = float(average_consumption * (deviation / 100))
                    average_consumption = random.uniform(average_consumption - limit, average_consumption + limit)
            elif simulation_duration_type == 'D':
                if float(deviation) == float(0):
                    average_consumption = 0.00 if pd.isna(row['Avrg. Consumption/Mnth']) else float(
                        row['Avrg. Consumption/Mnth'])
                    average_consumption = average_consumption / 30.416
                else:
                    average_consumption = 0.00 if pd.isna(row['Avrg. Consumption/Mnth']) else float(
                        row['Avrg. Consumption/Mnth'])

                    average_consumption = average_consumption / 30.416
                    limit = float(average_consumption * (deviation / 100))
                    average_consumption = random.uniform(average_consumption - limit, average_consumption + limit)

            diff = prev_stock - average_consumption

            if pd.isna(row['Prev_Order']):
                row[current_index] = diff

                if row[current_index] <= row['MIN (Reorder Point)']:
                    order = row['MAX (Order Up To)'] - diff
                    if simulation_duration_type == 'M':

                        if row['Rounded Lead Time'] < 1:
                            row[current_index] = diff + order
                            row['Prev_Order'] = pd.NA
                        else:
                            row['Prev_Order'] = str(int(current_index.lstrip(simulation_duration_type)) + math.floor(
                                row['Rounded Lead Time'])) + '+' + str(order)
                    else:
                        row['Prev_Order'] = str(
                            int(current_index.lstrip(simulation_duration_type)) + row['Rounded Lead Time']) + '+' + str(
                            order)
            else:
                if str(int(current_index.lstrip(simulation_duration_type))) == row['Prev_Order'].split('+')[0].rstrip('.0'):
                    row[current_index] = diff + float(row['Prev_Order'].split('+')[1])
                    row['Prev_Order'] = pd.NA

                    if row[current_index] <= row['MIN (Reorder Point)']:
                        order = row['MAX (Order Up To)'] - row[current_index]
                        row['Prev_Order'] = str(
                            int(current_index.lstrip(simulation_duration_type)) + row['Rounded Lead Time']) + '+' + str(
                            order)
                else:
                    row[current_index] = diff

            return row

        def sim_process_file(df, simulation_time, default_price):
            df = df.dropna(how='all')
            df = df.fillna(0)
            df = df.replace({0: pd.NA, '0': pd.NA, '': pd.NA, 'None': pd.NA})

            if simulation_time_type == 'months':
                df['Lead Time (months)'] = df['Lead Time (days)'].astype(float) / 30.416
                if self.ui.Round_LT.isChecked():
                    df['Rounded Lead Time'] = df['Lead Time (months)'].replace({pd.NA: 0}).round().astype(int)
                else:
                    df['Rounded Lead Time'] = df['Lead Time (months)'].replace({pd.NA: 0}).astype(float)
                simulation_duration_type = 'M'
            elif simulation_time_type == 'days':
                simulation_duration_type = 'D'
                df['Rounded Lead Time'] = df['Lead Time (days)'].replace({pd.NA: 0}).astype(float)

            df['Prev_Order'] = pd.NA

            for rep in range(simulation_time):
                df['{}{}'.format(simulation_duration_type, rep + 1)] = ''
                for ci in range(1, len(df) + 1):
                    row = df.loc[ci - 1]
                    new_row = sim_process_row(row, ci, simulation_duration_type)
                    df.loc[ci - 1] = new_row

            df.drop(columns=['Prev_Order'], inplace=True)

            fs_df = df[['ItemNumber', 'Description', 'Price/Unit']].copy()

            for column in range(simulation_time):
                colm_title = '{}{}'.format(simulation_duration_type, column + 1)
                price_column = df['Price/Unit']
                price_column.replace({pd.NA: default_price}, inplace=True)
                amount_column = df[colm_title] * price_column
                fs_df[colm_title] = amount_column

            def remove_neg(x):
                if 'M' in x.name:
                    return x.clip(lower=0)
                else:
                    return x

            if self.ui.Remove_Negs.isChecked():
                fs_df = fs_df.apply(remove_neg)

            fs_df.loc['Total'] = fs_df.sum(axis=0)
            fs_df.iloc[-1, 1] = ''
            fs_df.iloc[-1, 0] = 'Total'

            return df, fs_df

        def sim_save_output(df, fs_df):
            output_file = 'output/sim_output.xlsx'

            try:
                writer = pd.ExcelWriter(output_file, engine='openpyxl', mode='w+')

                df.to_excel(writer, sheet_name='Inventory Simulation', index=False)
                fs_df.to_excel(writer, sheet_name='Financial Simulation', index=False)

                writer.close()

                ExcelWorkbook = load_workbook(output_file)
                for sheet_name in ['Inventory Simulation', 'Financial Simulation']:
                    ws = ExcelWorkbook[sheet_name]
                    thin_border = Border(left=Side(style='thin'),
                                         right=Side(style='thin'),
                                         top=Side(style='thin'),
                                         bottom=Side(style='thin'))
                    max_column = ws.max_column + 1
                    max_row = ws.max_row + 1
                    for col in range(1, max_column):
                        ws.cell(1, col).fill = PatternFill("solid", start_color="d9e1f2")
                        for row in range(1, max_row):
                            ws.cell(row, col).border = thin_border
                            ws.cell(row, col).font = Font(name='Trebuchet MS')
                            if row == max_row - 1 and sheet_name == 'Financial Simulation':
                                ws.cell(row, col).fill = PatternFill("solid", start_color="C5D9F1")

                ExcelWorkbook.save(output_file)

            except Exception as e:
                print(e)
                print('Unable To Save File')

        simulation_time_type = 'months'  # Change this to your desired simulation time type
        default_price = 10.0  # Change this to your default price

        df, fs_df = sim_process_file(df, simulation_time, default_price)
        sim_save_output(df, fs_df)

        return render(request, 'simulate.html', {'result': 'Simulation completed and saved successfully.'})

    # Handle GET request here
    return render(request, 'simulate.html')


def index(request):
    if request.method == 'POST':
        lead_time = request.POST.get('lead_time')
        service_level = request.POST.get('service_level')
        review_period = request.POST.get('review_period')
        benchmark = request.POST.get('benchmark')
        browse = request.FILES.get('filedata')
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", lead_time)

        LT_Adjustment = 0 if lead_time in [None, 'None', '', ' '] else int(lead_time)
        Alpha = 0 if service_level in [None, 'None', '', ' '] else float(service_level)
        ReviewPeriod = 0 if review_period in [None, 'None', '', ' '] else float(review_period) / 30.41666667

        # Initialize or load your DataFrame (df1) here
        try:
            if browse is not None:
                df1 = pd.read_csv(browse)
            else:
                df1 = pd.DataFrame()  # Initialize an empty DataFrame if no file is uploaded
        except Exception as e:
            # Handle any potential errors when reading the file
            print("Error reading the file:", str(e))
            df1 = pd.DataFrame()  # Initialize an empty DataFrame as a fallback

        if not df1.empty:
            # Perform calculations on df1
            df1['Total'] = df1.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).sum(axis=1)
            df1['LifeTime'] = df1.iloc[:, start_col + 1:end_col].apply(opt_length, axis=1)
            df1['Min Order'] = df1.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).replace(
                {'0': pd.NA, 0: pd.NA}).min(axis=1)
            df1['Max Order'] = df1.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).max(axis=1)
            df1['Adjusted LT (days)'] = df1.iloc[:, end_col] + LT_Adjustment
            df1['Adjusted LT (month)'] = df1['Adjusted LT (days)'] / 30.41666667
            df1['Average Demand'] = df1['Total'] / df1['LifeTime']
            df1['Demand over LT'] = df1['Average Demand'] * df1['Adjusted LT (month)']
            df1['Std. Deviation of Demand'] = df1.iloc[:, start_col + 1:end_col].apply(opt_nonzerostd, 1)
            df1['Std. Dev. of Demand over LT'] = df1['Std. Deviation of Demand'] * np.sqrt(
                df1['Adjusted LT (month)'].astype(float))
            df1['Safety Stock'] = scipy.stats.norm.ppf(Alpha, 0, 1) * df1['Std. Dev. of Demand over LT']
            df1['Min'] = scipy.stats.norm.ppf(Alpha, 0, 1) * df1['Std. Dev. of Demand over LT'] + df1['Demand over LT']

            if benchmark == 'No BenchMark':
                df1['Adjusted MIN'] = df1['Min']
            elif benchmark == 'Current Min':
                df1['Adjusted MIN'] = np.where(df1['Min'] < current_min_col, current_min_col, df1['Min'])
            elif benchmark == 'Max Order':
                df1['Adjusted MIN'] = np.where(df1['Min'] < df1['Max Order'], df1['Max Order'], df1['Min'])
            elif benchmark == 'Both':
                max_result = np.where(current_min_col < df1['Max Order'], df1['Max Order'], current_min_col)
                df1['Adjusted MIN'] = np.where(df1['Min'] < max_result, max_result, df1['Min'])
            elif benchmark == 'Slow Moving Items':
                df1['Adjusted MIN'] = np.ceil(
                    np.where(df1['Demand over LT'] > 10, df1['Demand over LT'] + df1['Average Demand'],
                             df1['Demand over LT'] + 1)).astype(int)
                df1['MAX'] = np.ceil(df1['Adjusted MIN'] + df1['Demand over LT']).astype(int)

            elif benchmark == 'Compare All':
                df1['Adjusted MIN-No BenchMark'] = df1['Min']
                df1['Adjusted MIN-Current Min'] = np.where(df1['Min'] < current_min_col, current_min_col, df1['Min'])
                df1['Adjusted MIN-Max Order'] = np.where(df1['Min'] < df1['Max Order'], df1['Max Order'], df1['Min'])
                max_result = np.where(current_min_col < df1['Max Order'], df1['Max Order'], current_min_col)
                df1['Adjusted MIN-Both'] = np.where(df1['Min'] < max_result, max_result, df1['Min'])
                df1['Adjusted MIN-Slow Moving Items'] = np.ceil(
                    np.where(df1['Demand over LT'] > 10, df1['Demand over LT'] + df1['Average Demand'],
                             df1['Demand over LT'] + 1)).astype(int)

                df1['MAX-No BenchMark'] = (df1['Average Demand'] * ReviewPeriod) + df1['Adjusted MIN-No BenchMark']
                df1['MAX-Current Min'] = (df1['Average Demand'] * ReviewPeriod) + df1['Adjusted MIN-Current Min']
                df1['MAX-Max Order'] = (df1['Average Demand'] * ReviewPeriod) + df1['Adjusted MIN-Max Order']
                df1['MAX-Both'] = (df1['Average Demand'] * ReviewPeriod) + df1['Adjusted MIN-Both']
                df1['MAX-Slow Moving Items'] = np.ceil(df1['Adjusted MIN-Slow Moving Items'] + df1['Demand over LT']).astype(int)

            if benchmark != 'Slow Moving Items' and benchmark != 'Compare All':
                df1['MAX'] = (df1['Average Demand'] * ReviewPeriod) + df1['Adjusted MIN']

            if benchmark == 'Compare All':
                df1['Cycle Service Level-No BenchMark'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN-No BenchMark'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                df1['Cycle Service Level-Current Min'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN-Current Min'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                df1['Cycle Service Level-Max Order'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN-Max Order'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                df1['Cycle Service Level-Both'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN-Both'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                df1['Cycle Service Level-Slow Moving Items'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN-Slow Moving Items'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))
            else:
                df1['Cycle Service Level'] = scipy.stats.norm.cdf(
                    (df1['Adjusted MIN'].astype(float) + 0.0056).round(decimals=4),
                    df1['Demand over LT'].astype(float).round(decimals=3),
                    df1['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

            df1['Adjusted LT (month)'] = df1['Adjusted LT (month)'].astype(float).round(1)
            df1['Average Demand'] = df1['Average Demand'].astype(float).round(1)
            df1['Demand over LT'] = df1['Demand over LT'].astype(float).round(1)
            df1['Std. Deviation of Demand'] = df1['Std. Deviation of Demand'].astype(float).round(1)
            df1['Std. Dev. of Demand over LT'] = df1['Std. Dev. of Demand over LT'].astype(float).round(1)
            df1['Safety Stock'] = df1['Safety Stock'].astype(float).round(1)
            df1['Min'] = df1['Min'].astype(float).round(1)

            if benchmark == 'Compare All':
                for item in ['No BenchMark', 'Current Min', 'Max Order', 'Both', 'Slow Moving Items']:
                    df1['Adjusted MIN-{}'.format(item)] = df1['Adjusted MIN-{}'.format(item)].astype(float).round(1)
                    df1['MAX-{}'.format(item)] = df1['MAX-{}'.format(item)].astype(float).round(1)
                    df1['Cycle Service Level-{}'.format(item)] = df1['Cycle Service Level-{}'.format(item)].astype(
                        float).round(5)
            else:
                df1['Adjusted MIN'] = df1['Adjusted MIN'].astype(float).round(1)
                df1['MAX'] = df1['MAX'].astype(float).round(1)
                df1['Cycle Service Level'] = df1['Cycle Service Level'].astype(float).round(5)

            # Prepare data for rendering
            context = {
                'result_data': {
                    'LT_Adjustment': LT_Adjustment,
                    'Alpha': Alpha,
                    'ReviewPeriod': ReviewPeriod,
                    'benchmark': benchmark,
                    # Include other calculated values here
                },
                'df1_results': df1.to_dict(orient='records')
            }

            return render(request, 'index.html', context)
        else:
            # Handle the case where the DataFrame is empty or couldn't be loaded
            return render(request, 'index.html', {'error_message': 'Error loading or processing the file'})
    else:
        return render(request, 'index.html')
