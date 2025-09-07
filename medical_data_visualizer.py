import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['height'] = df['height']/100

bmi = df['weight']/(df['height'])**2

df['overweight'] = np.where(bmi > 25, 1, 0)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4
def draw_cat_plot():

    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )

    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    fig = sns.catplot(
        x="variable", 
        y="total", 
        hue="value", 
        col="cardio",
        data=df_cat, 
        kind="bar"
        ).fig

    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    
    df_heat =  df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))


    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(
            corr,
            mask=mask,
            annot=True,
            fmt=".1f",
            center=0,
            vmin=-0.1,
            vmax=0.25,
            cmap="coolwarm",
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": 0.5}
        )


    fig.savefig('heatmap.png')
    return fig
