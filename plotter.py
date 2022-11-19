import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("sapply.csv")
df = df.drop("Unnamed: 0", axis=1)
df.columns = [int(x)/3-10 for x in df.columns]
df.index = [-x/3+10 for x in df.index]
plot = sns.heatmap(df, square=True)
plt.show()