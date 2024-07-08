import pandas as pd
import itertools as it

xls = pd.ExcelFile('Mario Kart 8 Deluxe Stats.xlsx')
sheets = pd.read_excel(xls,sheet_name=None,header=1)

elements = []
c = []

def agg_stats(row):
    dfa = pd.concat(row.apply(lambda f: combined[combined['Element']==f]).to_list())
    return pd.concat([row,dfa.sum()[3:]],axis=0)

def assemble_list(item):
    if isinstance(item,tuple):
        return [item[len(item) - 1]] + assemble_list(item[0])
    else:
        return [item]

for i,s in enumerate(sheets.keys()):
    col = sheets[s].columns[2]
    print(col,s)
    if i==0:
        elements = sheets[s][col].to_list()
    else:
        elements = list(it.product(elements,sheets[s][col].to_list()))
    c.append(sheets[s].rename(columns={'Unnamed: 2':'Element'}))

combined = pd.concat(c)

for i, e in enumerate(elements):
    elements[i] = assemble_list(e)

print(elements)

df = pd.DataFrame(elements).rename(columns={0:'Glider',1:'Wheels',2:'Chassis',3:'Driver'}).dropna().reset_index()

df.apply(agg_stats,axis='columns')[1:].to_csv('all_builds.csv', index=False)

