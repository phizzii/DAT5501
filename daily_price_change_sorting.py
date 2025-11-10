# for 1 year asset price, calculate the daily change in price
# ^p = p(n+1) - p(n)
# time how long it takes T to sort ^p for n = 7 > 365
# plot T vs n, does it follow n log n distribution

from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from sqlalchemy import true

# creating relevant dataframe for historical data on Rocket Lab asset price

rocket_lab_historical_data_df = pd.read_csv("HistoricalData_1761069203394.csv")

# making the date column into datetime format
rocket_lab_historical_data_df['Date'] = pd.to_datetime(rocket_lab_historical_data_df['Date'])

# first take high and low columns, calculate the range, then create a new column for the range (daily price change)
# then create numpy array for daily price change and date columns only, syntax > a = df[['a','b']].to_numpy()

print(rocket_lab_historical_data_df.head())
# change pd into numpy array, NUMPY ARRAYS CAN ONLY BE ONE DATA TYPE THEREFORE CREATE SEPARATE NUMPY ARRAYS FOR EACH DATA TYPE

# NUMPY_rocket_lab_data_df = rocket_lab_historical_data_df

# google how to do sorts in python (different sorts) [bubble, insertion, merge, quick, tim]
#   PLAN: create functions for each sort and then create functions to measure the O time complexity of each function to compare how quick each of the sorts are

# creating functions in preparation for numpy array creation
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # flag for terminating function early if there is nothing to sort
        already_sorted = True

        # observe each element one by one then compare to adjacent value
        for j in range(n - i - 1):
            if array[j] > array [j + 1]:
                # if element being observed is greater than adjacent value then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # two elements were swapped so set flag to false so functions doesn't finish early
                already_sorted = False
        
        # if there were no swaps during last iteration then it is sorted and function stops
        if already_sorted:
            break
    
    return array
