### freeCodeCamp Forum Page Views Analysis
### Project Overview

This project visualizes daily page views on the freeCodeCamp.org forum from May 9, 2016, to December 3, 2019.
The aim is to explore trends, seasonal patterns, and growth in forum activity over time using time series data visualization.

The project demonstrates how to:

Analyze large datasets with Pandas.

Visualize data with Matplotlib and Seaborn.

Interpret trends, outliers, and seasonal patterns in forum activity.

### Features / Visualizations

Line Chart

Displays daily page views over the entire period.

Reveals overall trends, growth, and spikes in activity.

Bar Chart

Compares average monthly page views per year.

Highlights yearly growth and seasonal variations.

Box Plots

Shows distribution of page views by year and month.

Helps identify variability, outliers, and seasonal trends.

### Technologies Used

Python 3

Pandas – for data cleaning and manipulation

Matplotlib – for plotting line charts and customizing visuals

Seaborn – for advanced visualizations like bar charts and box plots

How It Works

The CSV dataset is imported using Pandas.

Data is cleaned by removing extreme outliers (top 2.5% and bottom 2.5% of page views).

Columns for year and month are extracted from the date.

Different plots are created to explore trends and seasonal patterns.

### Insights

Daily page views show long-term growth from 2016 to 2019.

Certain months and years consistently have higher activity.

Box plots reveal seasonal trends and extreme spikes in forum usage.
