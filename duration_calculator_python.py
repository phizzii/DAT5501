# write code to take a date input from the user and calculate how many days until today
# unit testing: build a test suite to validate your calculation
# code extension: load the dates from the random_dates.csv file on qm+
# write a function to calculate how many days in the past each date it
# hint use np.datetime64

import numpy as np

desired_date = input('input date (not current) in the format yyyy-mm-dd. e.g. 2007-03-09')
desired_date_in_dt = np.datetime64(desired_date)
print(desired_date_in_dt)

current_date = np.datetime64('today')
print(current_date)

days_difference = current_date - desired_date_in_dt

print(days_difference)