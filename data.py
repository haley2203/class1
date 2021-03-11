import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
print(df)
df.head().to_csv("iris_sample.csv")

