import pandas as pd

df = pd.read_csv("data//T.A-F1.csv")
df = df.drop('y', axis=1)

print(df)

print(list(df.columns[:1]))