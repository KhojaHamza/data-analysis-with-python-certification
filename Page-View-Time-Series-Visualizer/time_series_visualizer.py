import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
# CLEAN THE DATA 
df = pd.read_csv("fcc-forum-pageviews.csv",header=0,names =['date','page_views'])
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df.head(9)
low =  df['page_views'].quantile(0.025)
heigh =  df['page_views'].quantile(0.975)
mask = ~((df['page_views'] < low) | (df['page_views'] > heigh))
df =df[mask]
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df['date'], df['page_views'], color='red', linewidth=1)
        
    # Set title and labels
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Show grid
    ax.grid(True)
    fig.savefig("line_plot.png")
    return fig
def draw_bar_plot():
    df_bar = df.copy()
    
    # Add year and month columns
    df_bar['year'] = df['date'].dt.year

    df_bar['month'] = df['date'].dt.month
    
    # Group by year and month, calculate average page views
    df_grouped = df_bar.groupby(['year', 'month'])['page_views'].mean().unstack()
    
    # Month names for x-axis
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    # Draw bar plot
    colors = sb.color_palette("bright", 12)

    fig = df_grouped.plot(kind='bar', figsize=(18, 10), color=colors).figure
    
    # Set labels and title
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=months)
    
    fig.savefig("bar_plot.png")
    return fig
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Month as short name
    df_box['month_num'] = df_box['date'].dt.month        # Month as number for sorting
    df_box = df_box.sort_values('month_num')
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Year-wise box plot
    sb.boxplot(x='year', y='page_views', data=df_box, ax=axes[0],hue='year',palette='bright',dodge=False)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Month-wise box plot
    sb.boxplot(x='month', y='page_views', data=df_box, ax=axes[1],hue='month',palette='bright',dodge=False)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    # Save figure
    fig.savefig("box_plot.png")
    return fig
