import pandas as pd
from geopy import distance

def main():
    station_df = pd.read_csv('stations.csv')
    node_df = pd.read_csv('../Spatial_STL_SC/chicago_data_2018-10-08/nodes.csv')
    df = pd.DataFrame(index=node_df['node_id'],columns=['closest_station_id'])
    for index, row in node_df.iterrows():
        minDist = float('inf')
        minStationId = None
        for index2,row2 in station_df.iterrows():
            km_dist = distance.vincenty((row['lat'],row['lon']),(row2['lat'],row2['lon']))
            if km_dist < minDist:
                minDist = km_dist
                minStationId = row2['id']
        df.at[row['node_id'],'closest_station_id'] = minStationId
    df.to_csv('closest_station_list.csv')
main()
