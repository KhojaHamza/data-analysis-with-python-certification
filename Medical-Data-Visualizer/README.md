### Medical Data Visualizer

This project analyzes a medical examination dataset and creates visualizations to help understand the relationship between health metrics and cardiovascular disease.

### 📝 Description

The project includes two main functions:

draw_cat_plot()

Generates a categorical bar plot showing counts of patients with cardiovascular disease (cardio=1) and without (cardio=0) for features like cholesterol, glucose, alcohol consumption, smoking, activity, and overweight.

Normalizes the data so that 0 is always "good" and 1 is always "bad".

Saves the figure as catplot.png.

draw_heat_map()

Cleans the dataset by removing incorrect or extreme values:

Diastolic pressure higher than systolic

Height or weight outside the 2.5th–97.5th percentiles

Computes a correlation matrix of the cleaned dataset.

Plots a heatmap with only the upper triangle to avoid duplication.

Saves the figure as heatmap.png.

### 📂 Files

medical_examination.csv – Dataset with patient health metrics

medical_data_visualizer.py – Python script with plotting functions

catplot.png – Example output of categorical plot

heatmap.png – Example output of heatmap
