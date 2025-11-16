# download us election data on qm+
# load file into a pandas dataframe
# plot a histogram of the fraction of votes
# compare vote fraction for two candidates

import pandas as pd
import matplotlib.pyplot as plt

us_election_df = pd.read_csv('us_election_dataset.csv', sep=';') # cause its separated by semi colons

plt.hist(us_election_df['fraction_votes'], edgecolor='black')
plt.xlabel('Fraction of votes')
plt.ylabel('Count')
plt.title('Histogram of vote fractions')

plt.show()