from re import M
from turtle import color
from matplotlib import axes, markers
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

mask4 = uk_china_deaths_2011_to_2019_df['cause_name'] == ('Neurological disorders')
neuro_only_uk_china_deaths_2011_2019_df = uk_china_deaths_2011_to_2019_df[mask4]

mask5 =uk_china_deaths_2011_to_2019_df['cause_name'] == ('Mental disorders')
mental_only_uk_china_deaths_2011_2019_df = uk_china_deaths_2011_to_2019_df[mask5]

fig , ax1 = plt.subplots(figsize=(12,8))
colours = {'United Kingdom': 'royalblue', 'China': 'orange'}

ax2 = ax1.twinx()

for country in ['United Kingdom', 'China']:
    subset_neuro = neuro_only_uk_china_deaths_2011_2019_df[neuro_only_uk_china_deaths_2011_2019_df['location_name'] == country]
    ax1.bar(subset_neuro['year'] + (0.2 if country == 'China' else -0.2), (subset_neuro['val']/1000), width=0.4, color=colours[country], alpha=0.5, label=f'{country} deaths')

for country in ['United Kingdom', 'China']:
    subset_hours = uk_china_annual_working_hours_years_df[uk_china_annual_working_hours_years_df['Entity'] == country]
    ax2.plot(subset_hours['Year'], (subset_hours['Working hours per worker']/1000), color=colours[country], marker='o', linewidth=2, label=f'{country} working hours')

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Deaths caused by Neurological disorders (in thousands)', fontsize=14)
ax2.set_ylabel('Annual working hours per worker (in thousands)', fontsize=14)

ax1.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.title('Deaths caused by neurological disorders vs. working hours (UK versus China)', fontsize=12)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, bbox_to_anchor=(1.07, 1),loc='upper left')

plt.tight_layout(rect=[0,0,0.85,1])

#fig.subplots_adjust(right=0.8)
plt.show()

# mental disorder graph

fig , ax1 = plt.subplots(figsize=(12,8))
colours = {'United Kingdom': 'royalblue', 'China': 'orange'}

ax2 = ax1.twinx()

for country in ['United Kingdom', 'China']:
    subset_mental = mental_only_uk_china_deaths_2011_2019_df[mental_only_uk_china_deaths_2011_2019_df['location_name'] == country]
    ax1.bar(subset_mental['year'] + (0.2 if country == 'China' else -0.2), (subset_mental['val']), width=0.4, color=colours[country], alpha=0.5, label=f'{country} deaths')

for country in ['United Kingdom', 'China']:
    subset_hours = uk_china_annual_working_hours_years_df[uk_china_annual_working_hours_years_df['Entity'] == country]
    ax2.plot(subset_hours['Year'], (subset_hours['Working hours per worker']/1000), color=colours[country], marker='o', linewidth=2, label=f'{country} working hours')

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Deaths caused by mental disorders (in thousands)', fontsize=14)
ax2.set_ylabel('Annual working hours per worker (in thousands)', fontsize=14)

ax1.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.title('Deaths caused by mental disorders vs. working hours (UK versus China)', fontsize=12)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, bbox_to_anchor=(1.07, 1),loc='upper left')

plt.tight_layout(rect=[0,0,0.85,1])
axes.set_xticks(xticks, minor=True )
axes.grid('on', which='minor', axis='x' )
axes.grid('off', which='major', axis='x' )
#fig.subplots_adjust(right=0.8)
plt.show()


