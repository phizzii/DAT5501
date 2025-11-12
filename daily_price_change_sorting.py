# for 1 year asset price, calculate the daily change in price
# ^p = p(n+1) - p(n)
# time how long it takes T to sort ^p for n = 7 > 365
# plot T vs n, does it follow n log n distribution

from matplotlib import markers
from matplotlib.pylab import rand
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from sqlalchemy import true
from random import randint
from timeit import repeat

# creating relevant dataframe for historical data on Rocket Lab asset price

rocket_lab_historical_data_df = pd.read_csv("HistoricalData_1761069203394.csv")

# making the date column into datetime format
rocket_lab_historical_data_df['Date'] = pd.to_datetime(rocket_lab_historical_data_df['Date'])

# first take high and low columns, calculate the range, then create a new column for the range (daily price change)
# then create numpy array for daily price change and date columns only, syntax > a = df[['a','b']].to_numpy()

print(rocket_lab_historical_data_df.head())
# change pd into numpy array, NUMPY ARRAYS CAN ONLY BE ONE DATA TYPE THEREFORE CREATE SEPARATE NUMPY ARRAYS FOR EACH DATA TYPE

rocket_lab_historical_data_df['High'] = rocket_lab_historical_data_df['High'].str.removeprefix('$')

rocket_lab_historical_data_df['Low'] = rocket_lab_historical_data_df['Low'].str.removeprefix('$')

rocket_lab_historical_data_df['High'] = rocket_lab_historical_data_df['High'].astype(float)

rocket_lab_historical_data_df['Low'] = rocket_lab_historical_data_df['Low'].astype(float)

rocket_lab_historical_data_df['Price Change'] = rocket_lab_historical_data_df['High'] - rocket_lab_historical_data_df['Low']

NUMPY_rocket_lab_data_df = rocket_lab_historical_data_df[['Price Change']].astype(float).to_numpy()

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

def insertion_sort(array):
    # looping from second element of the array until the last one
    for i in range(1, len(array)):
        # element we want to position in correct place
        key_item = array[i]
        # create variable that will be used to find correct position of the element referenced by key_item variable
        j = i - 1

        # run through list of items (left portion of array) and find correct position of element referenced by key_item but only if key item is smaller than its adjacent values
        while j >= 0 and array[j] > key_item:
            # shift value one position to the left and reposition j to point to the next element in the list right to left
            array[j + 1] = array[j]
            j -= 1

            # when finished shifting elements, position key item in its correct locations
            array[j + 1] = key_item
        
        return array
    
def merge_sort(left, right):
    # if first array is empty nothing needs to be merged, return second array as result
    if len(left) == 0:
        return right

    # if second array is empty nothing needs to be merged, return first array as result
    if len(right) == 0:
        return left
    
    # create result array
    result = []
    index_left = index_right = 0

    # go through both arrays until all elements are in the result array
    while len(result) < len(left) + len(right):
        # elements that need to be sorted add them to result array (first or second)
        if left[index_left] <= right[index_right:
            result.append(left[index_right])]:
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # if end of either array is reached, add remaining elements from other array to result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result
            
def quick_sort(array):
    # if the array has less then 2 items then it is returned as the result of the function
    if len(array) <2:
        return array
    
    low, same, high = []

    # select the pivot element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # elements that are smaller than the pivot go to the low list, elements that are larger than the pivot goes to the high list and elements that are equal to the pivot go into the same list
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # the final result combines the sorted low list with the same list and high list
    return quick_sort(low) + same + quick_sort(high)

def run_sorting_algorithm(algorithm, array):
    # call specific algorithm with supplied array (the rocket lab past data price change)
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}(array)"

    # run the code to see how long it took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=1, globals={"array": array, algorithm: globals()[algorithm]})

    # display name of algorithm and minimum time taken to run (it was only run once so the first one)
    print(f"algorithm: {algorithm}. time taken: {min(times)}")

if __name__ == "__main__":
    run_sorting_algorithm(algorithm="bubble_sort", array=NUMPY_rocket_lab_data_df)
    run_sorting_algorithm(algorithm="insertion_sort", array=NUMPY_rocket_lab_data_df)
    run_sorting_algorithm(algorithm="merge_sort", array=NUMPY_rocket_lab_data_df)
    run_sorting_algorithm(algorithm="quick_sort", array=NUMPY_rocket_lab_data_df)