import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

# creating relevant data frames for csv files, specifying columns to be displayed
# datasets to go from 2011 to 2019 (9 years)
uk_china_deaths_df = pd.DataFrame("UK_vs_China_Death_Data.csv")
uk_china_annual_working_hours_df = pd.read_csv("annual-working-hours-per-worker.csv")

uk_china_deaths_df.head()