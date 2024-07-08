import pandas as pd

df = pd.read_csv('all_builds.csv')

print(df[df.columns[5:]].T.sum())
df['Total'] = df[df.columns[5:]].T.sum().T
df.sort_values(by='Total',ascending=False,inplace=True)

df.head(10).to_csv('top_ten_builds.csv',index=False)
df[df['Driver']=='Rosalina\nRst'].head(10).to_csv('rosi_builds.csv',index=False)