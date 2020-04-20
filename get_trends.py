import os
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

with open('activities.txt') as f:
    activities = f.read().strip().split('\n')

baseline_word = 'lissom'

# for activity in activities:
#     print(activity, end='\t')
#     pytrend.build_payload(kw_list=[baseline_word, activity], timeframe='today 3-m')
#     df = pytrend.interest_over_time()
#     if not df.empty:
#         df[activity].to_csv(os.path.join('results', 'bottom1', '_'.join(activity.strip().split(' ')) + '.csv'))
#         print('Done')
#     else:
#         print("Error")

# Without baseline
for activity in activities:
    print(activity, end='\t')
    pytrend.build_payload(kw_list=[activity], timeframe='today 3-m')
    df = pytrend.interest_over_time()
    if not df.empty:
        df[activity].to_csv(os.path.join('results', 'nothing', '_'.join(activity.strip().split(' ')) + '.csv'))
        print('Done')
    else:
        print("Error")
