from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import scipy.stats

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
