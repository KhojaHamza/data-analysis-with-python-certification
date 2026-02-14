### 🌊 Sea Level Predictor
### Project Overview

This project analyzes historical data of global average sea level changes since 1880 and uses linear regression to predict sea level rise through the year 2050. The goal is to visualize long-term trends and compare them with more recent changes to better understand how sea levels are rising over time.

### 📊 Dataset

Source: Environmental Protection Agency (EPA)

File: epa-sea-level.csv

Key Columns:

Year — the year of measurement

CSIRO Adjusted Sea Level — global average sea level (in inches)

### Tools & Libraries Used

Python

Pandas — for data loading and manipulation

Matplotlib — for data visualization

SciPy (scipy.stats.linregress) — for linear regression analysis

### Tasks Completed

Imported the dataset using Pandas

Created a scatter plot with:

X-axis: Year

Y-axis: CSIRO Adjusted Sea Level

Calculated and plotted a line of best fit using all available data

Extended the regression line to 2050 to predict future sea level rise

Created a second regression line using data from the year 2000 onward

Extended the second line to 2050 to show a prediction based on recent trends

Labeled axes and added the title "Rise in Sea Level"

### 📈 Visualization Explanation

The final plot displays:

Historical sea level data as scattered points

A long-term trend line showing overall sea level rise since 1880

A recent trend line showing how the rate of sea level rise has changed since 2000

This comparison highlights how recent acceleration in sea level rise can significantly affect future predictions.

### Project Context

This project is part of the FreeCodeCamp Data Analysis with Python certification.
