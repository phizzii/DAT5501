from re import M
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

# creating relevant data frames for csv files, specifying columns to be displayed
# datasets to go from 2011 to 2019 (9 years)
uk_china_deaths_df = pd.read_csv("UK_vs_China_Death_Data.csv")
annual_working_hours_df = pd.read_csv("annual-working-hours-per-worker.csv")

# applying head function to see current columns to decide which to drop
print(uk_china_deaths_df.head())
print(annual_working_hours_df.head())

# dropping unnecessary columns from death dataset
uk_china_deaths_columns_dropped_df = uk_china_deaths_df.drop(columns=['measure_id','location_id','sex_id','age_id','cause_id','metric_id','upper','lower'])
print(uk_china_deaths_columns_dropped_df)

# creating mask for specific years
mask1 = uk_china_deaths_columns_dropped_df['year'] >= 2011
uk_china_deaths_2011_to_2019_df = uk_china_deaths_columns_dropped_df[mask1]

print(uk_china_deaths_2011_to_2019_df)

# creating mask for specific c
mask2 = annual_working_hours_df['Entity'].isin(['United Kingdom','China'])
uk_china_annual_working_hours_df = annual_working_hours_df[mask2]

print(uk_china_annual_working_hours_df)

mask3 = uk_china_annual_working_hours_df['Year'] >= (2011)
uk_china_annual_working_hours_years_df = uk_china_annual_working_hours_df[mask3]

print(uk_china_annual_working_hours_years_df)

# graph for neuro deaths vs working hours both countries

#plt.figure(figsize=(12,10))
fig, axes = plt.subplots(figsize=(12,10))
plt.scatter((uk_china_annual_working_hours_years_df['Year']),(uk_china_deaths_2011_to_2019_df['val']), c=(uk_china_annual_working_hours_years_df['Working hours per worker']), s=150, cmap='Spectral', edgecolors='black')
plt.colorbar(label='Average working hours per worker')
plt.title('Number of neurological deaths versus working hours in the UK and China', fontsize=10)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deaths from neurological related diseases', figsize=12)
plt.grid(True)
plt.tight_layout
plt.show()