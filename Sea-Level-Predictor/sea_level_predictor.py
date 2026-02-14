import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
def draw_plot():
    # read csv fle
    df = pd.read_csv('epa-sea-level.csv')
    # clean nan value  
    df_clean = df[df['CSIRO Adjusted Sea Level'].notna()]
    # all data regression line
    result = linregress(df_clean['Year'], df_clean['CSIRO Adjusted Sea Level'])
    slope = result.slope       # pente
    intercept = result.intercept  # y-intercept
    years_all = list(range(df_clean['Year'].min(), 2051))
    sea_level_fit = [slope * year + intercept for year in years_all]
    # recent data regression line
    df_recent = df_clean[df_clean['Year'] >= 2000]
        
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope_recent = result_recent.slope       # pente_years > 2000
    intercept_recent = result_recent.intercept  # y-intercept_years >2000
    years_recent = list(range(2000, 2051))
    sea_level_fit_recent =[slope_recent * year + intercept_recent for year in years_recent]
        
    fig, ax = plt.subplots(figsize=(16, 12))
    # draw scatter plot
    ax.scatter(df_clean["Year"], df_clean["CSIRO Adjusted Sea Level"],color = '#1f77b4',s=30,label='Sea Level Data')
    # Create a regression line using all data onwards to predict sea level in 2050
    ax.plot(years_all, sea_level_fit, color='red', linewidth = 2, label='Best Fit Line (1880-Present)')
    # Create a regression line using data from 2000 onwards to predict sea level in 2050
    ax.plot(years_recent, sea_level_fit_recent, color='green', linewidth = 2, label='Best Fit Line (2000-Present)')
    ax.set_xlabel("Year")
    ax.set_ylabel("CSIRO Adjusted Sea Level")
    ax.set_title("Sea Level Over Time")
    ax.legend(fontsize=12)
    plt.grid(True)
    fig.savefig('sea_level_predictor_plot.png')
    plt.show()
    return fig
    


