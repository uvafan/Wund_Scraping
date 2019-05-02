import os
import pandas as pd
station_df = pd.read_csv('stations.csv')
for index,row in station_df.iterrows():
    try:
        os.mkdir('data/{}'.format(row['id']))
    except:
        pass
