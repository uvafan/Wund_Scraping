import pandas as pd
import sc_plot

def main():
    '''
    stations used, in order:
    Chicago Loop
    West Town
    Wicker Park
    Logan Square
    Ukranian Village
    United Center
    Troposphere Group
    West Loop
    Lakeshore East
    West Loop - Union Park
    '''
    station_df = pd.DataFrame({
    'lat': [41.88,41.89,41.91,41.91,41.89,41.88,41.87,41.88,41.89,41.88],
    'lon': [-87.63,-87.65,-87.68,-87.7,-87.69,-87.68,-87.63,-87.65,-87.62,-87.66]
    })
    node_df = pd.read_csv('../../AoT_Chicago.complete.2019-03-28/nodes.csv')
    sc_plot.plotTwoGroups(station_df,node_df)

main()
