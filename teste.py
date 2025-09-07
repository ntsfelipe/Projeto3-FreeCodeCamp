import pandas as pd
import numpy as np

df = pd.read_csv("medical_examination.csv")

df['height'] = df['height']/100

bmi = df['weight']/(df['height'])**2

df['overweight'] = np.where(bmi > 25, 1, 0)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


df.head()