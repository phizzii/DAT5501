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