import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datasets/02/dermatology_database_1.csv')

# remove age values with ?
df = df[df['age'] != '?']

# convert age to int
df['age'] = df['age'].astype(int)

#calculate mean
print(df['age'].mean())
print(df['age'].median())

# plot boxplot
sns.boxplot(x='age', data=df)
plt.show()

