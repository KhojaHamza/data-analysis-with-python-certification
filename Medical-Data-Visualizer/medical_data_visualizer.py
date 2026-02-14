import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv("medical_examination.csv")

def draw_cat_plot():
    # ADD OVERWEIGHT COLuMN 
    df['overweight'] = (df['weight'] / ((df['height']/100)**2) > 25).astype(int)

    # NORMALIZE DATA BY MAKING 0 ALWAYS BAD AND 1 ALWAYS GOOD
    df['cholesterol'] = (df['cholesterol']> 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)
   
    # CREATE THE DATA FRAME
    df_cat = pd.melt(
    df,
    id_vars =['cardio'],
    var_name='categories',
    value_vars = ['cholesterol','gluc','smoke','alco','active','overweight'],
    value_name = 'states')
    sb.set(style='whitegrid')
    # CREAT A CHART
    graphic = sb.catplot(
    data=df_cat,
    x='categories',
    hue='states',
    col='cardio',
    kind='count',
    palette='bright'
)

    graphic.set_axis_labels('categories', 'count')
    graphic.set_titles("Cardio = {col_name}")
    
    fig = graphic.fig
    fig.savefig('catplot.png')
    plt.show()
    return fig
def draw_heat_map():

    # CLEAN THE DATA 
    df_heat = df.copy()
    mask_height = (df_heat['height'] < df_heat['height'].quantile(0.025)) | (df_heat['height'] > df_heat['height'].quantile(0.975))
    mask_weight = (df_heat['weight'] < df_heat['weight'].quantile(0.025)) | (df_heat['weight'] > df_heat['weight'].quantile(0.975))
    mask_ap_lo = df_heat['ap_lo'] > df_heat['ap_hi']
    
    df_heat = df_heat[~(mask_ap_lo | mask_height | mask_weight)]

    #.....
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(8,6))

    sb.heatmap(
       corr,
       mask=mask,
       annot=True,
       cmap='coolwarm',
       fmt=".2f",
       center=0,
       ax=ax
)
    plt.show()
    
    fig.savefig('heatmap.png')
    return fig