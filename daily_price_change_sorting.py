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

# google how to do sorts in python (different sorts)