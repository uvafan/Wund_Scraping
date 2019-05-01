import pandas as pd
import sc_plot

def main():
    station_df = pd.read_csv('stations.csv')
    node_df = pd.read_csv('../Spatial_STL_SC/chicago_data_2018-10-08/nodes.csv')
    sc_plot.plotTwoGroups(station_df,node_df)

main()
