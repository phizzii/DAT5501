# download us election data on qm+
# load file into a pandas dataframe
# plot a histogram of the fraction of votes
# compare vote fraction for two candidates

from os import uname
import pandas as pd
import matplotlib.pyplot as plt

us_election_df = pd.read_csv('us_election_dataset.csv', sep=';') # cause its separated by semi colons

plt.hist(us_election_df['fraction_votes'], edgecolor='black')
plt.xlabel('Fraction of votes')
plt.ylabel('Count')
plt.title('Histogram of vote fractions')
plt.show()

candidate1 = us_election_df[us_election_df['candidate'] == 'Bernie Sanders']['fraction_votes']
candidate2 = us_election_df[us_election_df['candidate'] == 'Ted Cruz']['fraction_votes']
colors = ['green', 'orange']

# i want to make a box plot lol

myplot = plt.boxplot([candidate1, candidate2], labels=['Bernie Sanders', 'Ted Cruz'], patch_artist=True)
for patch, color in zip(myplot['boxes'], colors):
    patch.set_facecolor(color)

plt.ylabel('Fraction of votes')
plt.title('Vote fraction comparison Sanders vs Cruz')
plt.show()