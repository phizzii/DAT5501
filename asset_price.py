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
from sqlalchemy import true

# creating relevant dataframe for historical data on Rocket Lab asset price

rocket_lab_historical_data_df = pd.read_csv("HistoricalData_1761069203394.csv")

print(rocket_lab_historical_data_df.head())

# making the date column into datetime format
rocket_lab_historical_data_df['Date'] = pd.to_datetime(rocket_lab_historical_data_df['Date'])

# making data frames per month (jan to dec)
# jan
jan_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '01-01-2025') & (rocket_lab_historical_data_df['Date'] <= '01-31-2025')

jan_rocket_lab_df = rocket_lab_historical_data_df.loc[jan_rocket_lab_df]

jan_rocket_lab_df['Day'] = jan_rocket_lab_df['Date'].dt.day
#print(jan_rocket_lab_df)

# feb
feb_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '02-01-2025') & (rocket_lab_historical_data_df['Date'] <= '02-28-2025')

feb_rocket_lab_df = rocket_lab_historical_data_df.loc[feb_rocket_lab_df]

feb_rocket_lab_df['Day'] = feb_rocket_lab_df['Date'].dt.day
#print(feb_rocket_lab_df)

# mar
mar_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '03-01-2025') & (rocket_lab_historical_data_df['Date'] <= '03-31-2025')

mar_rocket_lab_df = rocket_lab_historical_data_df.loc[mar_rocket_lab_df]

mar_rocket_lab_df['Day'] = mar_rocket_lab_df['Date'].dt.day
#print(mar_rocket_lab_df)

# apr
apr_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '04-01-2025') & (rocket_lab_historical_data_df['Date'] <= '04-30-2025')

apr_rocket_lab_df = rocket_lab_historical_data_df.loc[apr_rocket_lab_df]

apr_rocket_lab_df['Day'] = apr_rocket_lab_df['Date'].dt.day
#print(apr_rocket_lab_df)

# may
may_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '05-01-2025') & (rocket_lab_historical_data_df['Date'] <= '05-31-2025')

may_rocket_lab_df = rocket_lab_historical_data_df.loc[may_rocket_lab_df]

may_rocket_lab_df['Day'] = may_rocket_lab_df['Date'].dt.day
#print(may_rocket_lab_df)

# jun
jun_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '06-01-2025') & (rocket_lab_historical_data_df['Date'] <= '06-30-2025')

jun_rocket_lab_df = rocket_lab_historical_data_df.loc[jun_rocket_lab_df]

jun_rocket_lab_df['Day'] = jun_rocket_lab_df['Date'].dt.day
#print(jun_rocket_lab_df)

# jul
jul_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '07-01-2025') & (rocket_lab_historical_data_df['Date'] <= '07-31-2025')

jul_rocket_lab_df = rocket_lab_historical_data_df.loc[jul_rocket_lab_df]

jul_rocket_lab_df['Day'] = jul_rocket_lab_df['Date'].dt.day
#print(jul_rocket_lab_df)

# aug
aug_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '08-01-2025') & (rocket_lab_historical_data_df['Date'] <= '08-31-2025')

aug_rocket_lab_df = rocket_lab_historical_data_df.loc[aug_rocket_lab_df]

aug_rocket_lab_df['Day'] = aug_rocket_lab_df['Date'].dt.day
#print(aug_rocket_lab_df)

# sep
sep_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '09-01-2025') & (rocket_lab_historical_data_df['Date'] <= '09-30-2025')

sep_rocket_lab_df = rocket_lab_historical_data_df.loc[sep_rocket_lab_df]

sep_rocket_lab_df['Day'] = sep_rocket_lab_df['Date'].dt.day
#print(sep_rocket_lab_df)

# oct
oct_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '10-01-2025') & (rocket_lab_historical_data_df['Date'] <= '10-31-2025')

oct_rocket_lab_df = rocket_lab_historical_data_df.loc[oct_rocket_lab_df]

oct_rocket_lab_df['Day'] = oct_rocket_lab_df['Date'].dt.day
#print(oct_rocket_lab_df)

# nov
nov_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '11-01-2024') & (rocket_lab_historical_data_df['Date'] <= '11-30-2024')

nov_rocket_lab_df = rocket_lab_historical_data_df.loc[nov_rocket_lab_df]

nov_rocket_lab_df['Day'] = nov_rocket_lab_df['Date'].dt.day
#print(nov_rocket_lab_df)

# dec
dec_rocket_lab_df = (rocket_lab_historical_data_df['Date'] >= '12-01-2024') & (rocket_lab_historical_data_df['Date'] <= '12-31-2024')

dec_rocket_lab_df = rocket_lab_historical_data_df.loc[dec_rocket_lab_df]

dec_rocket_lab_df['Day'] = dec_rocket_lab_df['Date'].dt.day
#print(dec_rocket_lab_df)

# creating visual for jan prices as line graph

#print(jan_rocket_lab_df['Close/Last'].dtypes())
fig, axes = plt.subplots(figsize=(10,8))

#plt.scatter(jan_rocket_lab_df['Day'],jan_rocket_lab_df['Close/Last'], s=100)
#plt.plot(jan_rocket_lab_df['Date'])
plt.plot(jan_rocket_lab_df['Day'],jan_rocket_lab_df['Close/Last'], linewidth=1.8)
plt.title
plt.xlabel("Date in Jan", fontsize=14)
plt.ylabel("Closing Asset Price", fontsize=14)
plt.xticks(np.arange(0, 31, step=2))
#plt.yticks(np.arange(24, 32, step=0.5))
#axes.set_xticks(xticks, minor=True)
axes.grid('on', which='minor', axis='x' )
axes.grid('on', which='major', axis='x' )
plt.grid(True)
#plt.tight_layout
plt.show()

