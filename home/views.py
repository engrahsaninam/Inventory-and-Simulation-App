from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import scipy.stats


def opt_nonzerostd(self, row):
    row = self.opt_filtered_row(row)
    row = row.replace({0: pd.NA, '0': pd.NA, '': pd.NA, 'None': pd.NA})
    row = pd.Series(row.dropna().reset_index(drop=True))

    return row.std(ddof=0)


def opt_filtered_row(self, row):
    first_index = row.replace({0: pd.NA, '0': pd.NA, '': pd.NA, 'None': pd.NA}).first_valid_index()
    row = row[first_index:]
    row = row.fillna(0)
    return pd.Series(row.replace({pd.NA: 0}))


def opt_length(self, row):
    return len(self.opt_filtered_row(row))



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
                df = pd.read_excel(browse)
            else:
                df = pd.DataFrame()  # Initialize an empty DataFrame if no file is uploaded
        except Exception as e:
            # Handle any potential errors when reading the file
            print("Error reading the file:", str(e))
            df = pd.DataFrame()  # Initialize an empty DataFrame as a fallback
        
        if not df.empty:
            try:
                df = df.dropna(how='all')
                df = df.fillna(0)
                df = df.replace({0: pd.NA, '0': pd.NA, '': pd.NA, 'None': pd.NA})

                start_col = df.columns.get_loc('Description')

                end_col = len(df.columns) - 3
                current_min_col = df.iloc[:, end_col + 1]
                current_max_col = df.iloc[:, end_col + 2]

                # Perform calculations on df1
                df['Total'] = df.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).sum(axis=1)
                df['LifeTime'] = df.iloc[:, start_col + 1:end_col].apply(opt_length, axis=1)
                df['Min Order'] = df.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).replace(
                    {'0': pd.NA, 0: pd.NA}).min(axis=1)
                df['Max Order'] = df.iloc[:, start_col + 1:end_col].apply(opt_filtered_row, axis=1).max(axis=1)
                df['Adjusted LT (days)'] = df.iloc[:, end_col] + LT_Adjustment
                df['Adjusted LT (month)'] = df['Adjusted LT (days)'] / 30.41666667
                df['Average Demand'] = df['Total'] / df['LifeTime']
                df['Demand over LT'] = df['Average Demand'] * df['Adjusted LT (month)']
                df['Std. Deviation of Demand'] = df.iloc[:, start_col + 1:end_col].apply(opt_nonzerostd, 1)
                df['Std. Dev. of Demand over LT'] = df['Std. Deviation of Demand'] * np.sqrt(
                    df['Adjusted LT (month)'].astype(float))
                df['Safety Stock'] = scipy.stats.norm.ppf(Alpha, 0, 1) * df['Std. Dev. of Demand over LT']
                df['Min'] = scipy.stats.norm.ppf(Alpha, 0, 1) * df['Std. Dev. of Demand over LT'] + df['Demand over LT']

                if benchmark == 'No BenchMark':
                    df['Adjusted MIN'] = df['Min']
                elif benchmark == 'Current Min':
                    df['Adjusted MIN'] = np.where(df['Min'] < current_min_col, current_min_col, df['Min'])
                elif benchmark == 'Max Order':
                    df['Adjusted MIN'] = np.where(df['Min'] < df['Max Order'], df['Max Order'], df['Min'])
                elif benchmark == 'Both Current Min & Max Order':
                    max_result = np.where(current_min_col < df['Max Order'], df['Max Order'], current_min_col)
                    df['Adjusted MIN'] = np.where(df['Min'] < max_result, max_result, df['Min'])
                elif benchmark == 'Slow Moving Items':
                    df['Adjusted MIN'] = np.ceil(
                        np.where(df['Demand over LT'] > 10, df['Demand over LT'] + df['Average Demand'],
                                 df['Demand over LT'] + 1)).astype(int)
                    df['MAX'] = np.ceil(df['Adjusted MIN'] + df['Demand over LT']).astype(int)

                elif benchmark == 'Compare All':
                    df['Adjusted MIN-No BenchMark'] = df['Min']
                    df['Adjusted MIN-Current Min'] = np.where(df['Min'] < current_min_col, current_min_col, df['Min'])
                    df['Adjusted MIN-Max Order'] = np.where(df['Min'] < df['Max Order'], df['Max Order'], df['Min'])
                    max_result = np.where(current_min_col < df['Max Order'], df['Max Order'], current_min_col)
                    df['Adjusted MIN-Both Current Min & Max Order'] = np.where(df['Min'] < max_result, max_result, df['Min'])
                    df['Adjusted MIN-Slow Moving Items'] = np.ceil(
                        np.where(df['Demand over LT'] > 10, df['Demand over LT'] + df['Average Demand'],
                                 df['Demand over LT'] + 1)).astype(int)

                    df['MAX-No BenchMark'] = (df['Average Demand'] * ReviewPeriod) + df['Adjusted MIN-No BenchMark']
                    df['MAX-Current Min'] = (df['Average Demand'] * ReviewPeriod) + df['Adjusted MIN-Current Min']
                    df['MAX-Max Order'] = (df['Average Demand'] * ReviewPeriod) + df['Adjusted MIN-Max Order']
                    df['MAX-Both Current Min & Max Order'] = (df['Average Demand'] * ReviewPeriod) + df['Adjusted MIN-Both']
                    df['MAX-Slow Moving Items'] = np.ceil(df['Adjusted MIN-Slow Moving Items'] + df['Demand over LT']).astype(int)

                if benchmark != 'Slow Moving Items' and benchmark != 'Compare All':
                    df['MAX'] = (df['Average Demand'] * ReviewPeriod) + df['Adjusted MIN']

                if benchmark == 'Compare All':
                    df['Cycle Service Level-No BenchMark'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN-No BenchMark'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                    df['Cycle Service Level-Current Min'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN-Current Min'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                    df['Cycle Service Level-Max Order'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN-Max Order'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                    df['Cycle Service Level-Both Current Min & Max Order'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN-Both Current Min & Max Order'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                    df['Cycle Service Level-Slow Moving Items'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN-Slow Moving Items'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))
                else:
                    df['Cycle Service Level'] = scipy.stats.norm.cdf(
                        (df['Adjusted MIN'].astype(float) + 0.0056).round(decimals=4),
                        df['Demand over LT'].astype(float).round(decimals=3),
                        df['Std. Dev. of Demand over LT'].replace({0: 0.001}).astype(float).round(decimals=4))

                df['Adjusted LT (month)'] = df['Adjusted LT (month)'].astype(float).round(1)
                df['Average Demand'] = df['Average Demand'].astype(float).round(1)
                df['Demand over LT'] = df['Demand over LT'].astype(float).round(1)
                df['Std. Deviation of Demand'] = df['Std. Deviation of Demand'].astype(float).round(1)
                df['Std. Dev. of Demand over LT'] = df['Std. Dev. of Demand over LT'].astype(float).round(1)
                df['Safety Stock'] = df['Safety Stock'].astype(float).round(1)
                df['Min'] = df['Min'].astype(float).round(1)

                if benchmark == 'Compare All':
                    for item in ['No BenchMark', 'Current Min', 'Max Order', 'Both Current Min & Max Order', 'Slow Moving Items']:
                        df['Adjusted MIN-{}'.format(item)] = df['Adjusted MIN-{}'.format(item)].astype(float).round(1)
                        df['MAX-{}'.format(item)] = df['MAX-{}'.format(item)].astype(float).round(1)
                        df['Cycle Service Level-{}'.format(item)] = df['Cycle Service Level-{}'.format(item)].astype(
                            float).round(5)
                else:
                    df['Adjusted MIN'] = df['Adjusted MIN'].astype(float).round(1)
                    df['MAX'] = df['MAX'].astype(float).round(1)
                    df['Cycle Service Level'] = df['Cycle Service Level'].astype(float).round(5)

                # Prepare data for rendering
                context = {
                    'result_data': {
                        'LT_Adjustment': LT_Adjustment,
                        'Alpha': Alpha,
                        'ReviewPeriod': ReviewPeriod,
                        'benchmark': benchmark,
                        # Include other calculated values here
                    },
                    'df1_results': df.to_dict(orient='records')
                }

                return render(request, 'index.html', context)
            except Exception as e:
                # Handle the case where the DataFrame is empty or couldn't be loaded
                return render(request, 'index.html', {'error_message': 'Error Alert '+str(e)})
        else:
            # Handle the case where the DataFrame is empty or couldn't be loaded
            return render(request, 'index.html', {'error_message': 'Error loading or processing the file'})
    else:
        return render(request, 'index.html')
