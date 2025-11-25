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
cherry_blossom_df = pd.read_csv("datasets/date-of-the-peak-cherry-tree-blossom-in-kyoto.csv")

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
degree = 10

# as a for loop
def polyall():
    for i in range(1,degree):
        coefficients = np.polyfit(years_centered, peak, i)
        p = np.poly1d(coefficients)
        plt.figure(figsize=(10,6))
        plt.scatter(years, peak, label='Data points', color='blue')
        plt.plot(xp, p(xp_centered), label=f'order {i}', linewidth=2)
        plt.xlabel("Year")
        plt.ylabel("Peak days")
        plt.title(f"polynomial fit {i} year forecast")
        plt.legend()
        plt.show()

polyall()

# do chi squared first then do the following (get the residuals)
# for each polynomial, calculate the x^2 per degree of freedom and the BIC (X^2 + Np ln(No)) where No is the number of observations and Np is the number of parameters
# number of 'degrees of freedom' = No - Np where No is the number of observations and Np is the number of parameters
# plot X^2 per degree of freedom and the BIC as a function of the polynomial order
# how does BIC compare to the X^2 per degree of freedom - which model is best

# what are parameter values and covariance matrix
# what are the uncertainties in parameter values
# is there a better model for example exponential

# this is the test and train split

last_year = cherry_blossom_df['Year'].max()

train_df = cherry_blossom_df[cherry_blossom_df['Year'] <= last_year - 10]
test_df = cherry_blossom_df[cherry_blossom_df['Year'] > last_year - 10]

x_train = train_df['Year']
y_train = train_df['Peak day']

x_test = test_df['Year']
y_test = test_df['Peak day']

# center the data cause otherwise it goes alllll over the place
x_mean = x_train.mean()
x_train_c = x_train - x_mean
x_test_c = x_test - x_mean

# make lists for eval
orders = range(1,10)
chi2_vals = []
chi2_dof_vals = []
bic_vals = []

# looping through poly orders
uncertainty = 1.0 # just guessing the measurement uncertainty right now

for n in orders:
    # fit polynomial to training data, coeffs cause i already used coefficients :(
    coeffs = np.polyfit(x_train_c, y_train, n)
    model = np.poly1d(coeffs)

    # residuals (training)
    residuals = y_train - model(x_train_c)

    # chi-squared
    chi2 = np.sum((residuals / uncertainty)**2)
    chi2_vals.append(chi2)

    # degrees of freedom = Nobs - Nparams
    dof = len(x_train) - (n + 1)
    chi2_dof_vals.append(chi2 / dof)

    # BIC = chi² + k ln(N)
    bic = chi2 + (n + 1) * np.log(len(x_train))
    bic_vals.append(bic)

