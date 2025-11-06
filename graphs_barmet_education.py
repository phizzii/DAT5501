import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

def main(general_csv_path, results_csv_path, show_plots=True):
    dfGCSE = pd.read_csv('/Users/sophieb/Documents/csvGCSE.csv')
    df = pd.read_csv('/Users/sophieb/Documents/gcse results csv.csv')

    fig, axes = plt.subplots(figsize=(12,6))
    axes = df['average point score'].plot.kde(color='r',linestyle='-',linewidth=3)
    axes.set_xlabel('Average Point Score Per Candidate', fontsize=15)
    axes.set_ylabel('Density',fontsize=12)
    axes.tick_params(labelsize=12)

    mean = df['average point score'].mean()
    median = df['average point score'].median()

    axes.axvline(mean, color='green',linestyle='--',linewidth=2, label="Mean")
    axes.axvline(median, color='blue', linestyle='--', linewidth=2, label='Median')
    axes.set_title("Average Point Score per candidate")
    axes.annotate(f"Mean={mean:5.2f}", xy=(730,0.008))
    axes.annotate(f"Median={median:5.2f}", xy=(748,0.007))
    
    plt.legend()
    plt.show()

    data = pd.DataFrame(df)
    colors = ['royalblue','orange','orchid','forestgreen','gold','red']
    year = data['year'].head(8)
    entries = data['16-18 entered for L3'].head(8)
    fig = plt.figure(figsize=(10,7))
    plt.bar(year[0:10], entries[0:10], color=colors, edgecolor='black', linewidth=1)
    plt.ylabel('Number of 16-18 year olds', fontsize=15)
    plt.title('Number of students being entered for Level 3 Qualifications each year from 2009-2014', fontsize=15)
    plt.xlabel('Year', fontsize=15)
    plt.show()

    plt.figure(figsize=(12,6))
    plt.scatter(df['year'],df['% achieving at least 2 L3 qualifications (per candidate)'], c=df['% achieving at least 2 L3 qualifications (per candidate)'], s=200, cmap='Spectral')
    plt.ylabel('Percentage of students achieving \nat least 2 Level 3 Qualifications', fontsize=12)
    plt.xlabel('Year', fontsize=12)
    plt.title('Percentage of Students in Barnet achieving \nat least 2 Level 3 Qualifications from 2009 - 2014')
    plt.colorbar()
    
    if show_plots:
        plt.show()

    return {
        "mean": mean,
        "median": median,
        "num_rows": len(df),
        "num_cols": len(df.columns)
    }

if __name__ == "__main__":
    main(
        '/Users/sophieb/Documents/csvGCSE.csv'
        '/Users/sophieb/Documents/gcse results csv.csv'
        show_plots=True
    )
    