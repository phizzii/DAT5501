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

rocket_lab_historical_data = pd.read_csv("")