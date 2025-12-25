import pandas as pd

df = pd.read_csv("raw_data/accepted_2007_to_2018Q4.csv", nrows=5)
print(df)
print(df.columns)
print(df.describe())
df.to_csv("data/accepted.csv", index=False)
print("------------------------------------------------")

df = pd.read_csv("raw_data/rejected_2007_to_2018Q4.csv", nrows=5)
print(df)
print(df.columns)

print(df.describe())
df.to_csv("data/rejected.csv", index=False)
print("------------------------------------------------")

