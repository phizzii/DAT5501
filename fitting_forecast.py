# find dataset that measures a global trend over the past 10 years like population, temperature, gdp, life expectancy
# sub sample all but the past 10 years of data
# fit the sub-sample with polynomials from order 1 (a line) to 9 ax^n
# forecast each polynomial 10 years into the future
# how do they compare with reality

# import relevant modules
from re import M
from turtle import color
from matplotlib import axes, markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# making data frames for csv files
cherry_blossom_df = pd.read_csv("date-of-the-peak-cherry-tree-blossom-in-kyoto.csv")

# applying head() function to see current columns and decide which ones need to be displayed or dropped
print(cherry_blossom_df.head())

# dropping unnecessary columns from dataset
cherry_blossom_df = cherry_blossom_df.drop(columns=['Entity','Code'])
print(cherry_blossom_df.head())

# changing column names because they do not need to be that long lol
cherry_blossom_df.rename(columns={'Twenty-year average day of the year with peak cherry blossom': '20 yr rolling average peak day', 'Day of the year with peak cherry blossom': 'Peak day'}, inplace=True)
print(cherry_blossom_df.head())

# creating masks for specific years
mask1 = cherry_blossom_df['Year'] >= 1925
mask2 = cherry_blossom_df['Year'] <= 2015

first_range_cherry_blossom_df = cherry_blossom_df[mask1]
range_cherry_blossom_df = first_range_cherry_blossom_df[mask2]

print(range_cherry_blossom_df.head())

# attempt at trying to make polynomial fits for the graph
# remember y is peak day and x is year
years = range_cherry_blossom_df['Year']
years_centered = years - years.mean()
peak = range_cherry_blossom_df['Peak day']

xp = np.linspace(years.min(), years.max() + 10, 300)
xp_centered = xp - years.mean()

degree = 6

coefficients = np.polyfit(years_centered, peak, degree)
p = np.poly1d(coefficients)

plt.figure(figsize=(10,6))
plt.scatter(years, peak, label='Data points', color='blue')
plt.plot(xp, p(xp_centered), label=f'order {degree}', linewidth=2)

plt.xlabel("Year")
plt.ylabel("Peak days")
plt.title("polynomial fits 1-9 and 10 year forecast")
plt.legend()
plt.show()


