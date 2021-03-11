import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')
df.head().to_csv("iris_sample.csv")
df

