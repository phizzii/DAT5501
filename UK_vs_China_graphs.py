import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

# creating relevant data frames for csv files, specifying columns to be displayed
# datasets to go from 2011 to 2019 (9 years)
uk_china_deaths_df = pd.read_csv("UK_vs_China_Death_Data.csv")
uk_china_annual_working_hours_df = pd.read_csv("annual-working-hours-per-worker.csv")

# applying head function to see current columns to decide which to drop
print(uk_china_deaths_df.head())
print(uk_china_annual_working_hours_df.head())

# dropping unnecessary columns from death dataset
uk_china_deaths_df.drop(columns=['measure_id','location_id','sex_id','age_id','cause_id','metric_id','upper','lower'])

# creating mask for specific years
mask1 = uk_china_deaths_df['year'] >= 2011
uk_china_deaths_2011_to_2019_df = uk_china_deaths_df[mask1]

print(uk_china_deaths_2011_to_2019_df)
