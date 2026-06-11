import pandas as pd
import numpy as np

ipl = pd.read_csv('deliveries.csv')
print(ipl.head())
total_runs =  ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)

# print(total_runs)

max_sixs = ipl[ipl['batsman_runs'] == 6]
print(max_sixs.groupby('batsman')['batsman'].count())