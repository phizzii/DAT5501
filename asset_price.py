# choose a company on Nasdaq
# download 1 year of historical price data
# clean dataset as necessary
# plot closing price vs date
# extra: calculate daily percentage change, plot vs date
# extra extra: calculate standard deviation of percent daily changes

from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

# creating relevant dataframe for historical data on Rocket Lab asset price

rocket_lab_historical_data_df = pd.read_csv("HistoricalData_1761069203394.csv")

print(rocket_lab_historical_data_df.head())

# making the date column into datetime format
rocket_lab_historical_data_df['Date'] = pd.to_datetime(rocket_lab_historical_data_df['Date'])

# making data frames per month (jan to dec)
# jan
jan_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '01-01-2025') & (rocket_lab_historical_data_df['Date'] <= '01-31-2025')

jan_rocket_lab_df = rocket_lab_historical_data_df.loc[jan_rocket_lab_df]

print(jan_rocket_lab_df)

# feb
feb_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '02-01-2025') & (rocket_lab_historical_data_df['Date'] <= '02-28-2025')

feb_rocket_lab_df = rocket_lab_historical_data_df.loc[feb_rocket_lab_df]

print(feb_rocket_lab_df)

# mar
mar_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '03-01-2025') & (rocket_lab_historical_data_df['Date'] <= '03-31-2025')

mar_rocket_lab_df = rocket_lab_historical_data_df.loc[mar_rocket_lab_df]

print(mar_rocket_lab_df)

# apr
apr_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '04-01-2025') & (rocket_lab_historical_data_df['Date'] <= '04-30-2025')

apr_rocket_lab_df = rocket_lab_historical_data_df.loc[apr_rocket_lab_df]

print(apr_rocket_lab_df)

# may
may_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '05-01-2025') & (rocket_lab_historical_data_df['Date'] <= '05-31-2025')

may_rocket_lab_df = rocket_lab_historical_data_df.loc[may_rocket_lab_df]

print(may_rocket_lab_df)

# jun
jun_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '06-01-2025') & (rocket_lab_historical_data_df['Date'] <= '06-30-2025')

jun_rocket_lab_df = rocket_lab_historical_data_df.loc[jun_rocket_lab_df]

print(jun_rocket_lab_df)

# jul
jul_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '07-01-2025') & (rocket_lab_historical_data_df['Date'] <= '07-31-2025')

jul_rocket_lab_df = rocket_lab_historical_data_df.loc[jul_rocket_lab_df]

print(jul_rocket_lab_df)

# aug
aug_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '08-01-2025') & (rocket_lab_historical_data_df['Date'] <= '08-31-2025')

aug_rocket_lab_df = rocket_lab_historical_data_df.loc[aug_rocket_lab_df]

print(aug_rocket_lab_df)

# sep
sep_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '09-01-2025') & (rocket_lab_historical_data_df['Date'] <= '09-30-2025')

sep_rocket_lab_df = rocket_lab_historical_data_df.loc[sep_rocket_lab_df]

print(sep_rocket_lab_df)

# oct
oct_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '10-01-2025') & (rocket_lab_historical_data_df['Date'] <= '10-31-2025')

oct_rocket_lab_df = rocket_lab_historical_data_df.loc[oct_rocket_lab_df]

print(oct_rocket_lab_df)

# nov
nov_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '11-01-2024') & (rocket_lab_historical_data_df['Date'] <= '11-30-2024')

nov_rocket_lab_df = rocket_lab_historical_data_df.loc[nov_rocket_lab_df]

print(nov_rocket_lab_df)

# dec
dec_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '12-01-2024') & (rocket_lab_historical_data_df['Date'] <= '12-31-2024')

dec_rocket_lab_df = rocket_lab_historical_data_df.loc[dec_rocket_lab_df]

print(dec_rocket_lab_df)