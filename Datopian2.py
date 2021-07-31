import pandas as pd
import csv
from matplotlib import pyplot as plt
pd.set_option('display.max_columns', 500)
tableswp=pd.read_html('https://en.wikipedia.org/wiki/Road_safety_in_Europe', match='European Union Road Safety Facts and Figures')
print("Total Tables: ", len(tableswp))
df=tableswp[0]
df.rename(columns={'Area (thousands of km2)[24]':'Area', 'Population in 2018[25]':'Population', 'GDP per capita in 2018[26]':'GDP Per Capita', 'Population density (inhabitants per km2) in 2017[27]':'Population Density', 'Vehicle ownership (per thousand inhabitants) in 2016[28]':'Vehicle Ownership', 'Road Network Length (in km) in 2013[29]':'Road Network Length', 'Total Road Deaths in 2018[30]':'Total Road Deaths', 'Road deaths per Million Inhabitants in 2018[30]':'Road Deaths Per Million Inhabitants'}, inplace=True)
reqcols=['Country', 'Area', 'Population', 'GDP Per Capita', 'Population Density', 'Vehicle Ownership', 'Total Road Deaths', 'Road Deaths Per Million Inhabitants']
colms=list(df)
dcol=[]
for i in df.columns:
    if i not in reqcols:
        dcol.append(i)
df.drop(dcol, axis=1, inplace=True)
df.insert(1, 'Year', 2018)
df['GDP Per Capita']=df['GDP Per Capita'].replace('†a', '', regex=True)
df['GDP Per Capita']=df['GDP Per Capita'].replace(',', '', regex=True)
df['Population']=df['Population'].astype(str)
df['Population']=df['Population'].str.replace('.', '', regex=True)
df['Population']=df['Population'].str.replace(',', '', regex=True)
df['GDP Per Capita']=df['GDP Per Capita'].astype(int)
df['Population']=df['Population'].astype(int)
#print(df.head(2))
x=df.columns.get_loc("Population Density")
lpop=list(df['Population'])
larea=list(df['Area'])
newarea=[]
for k in range(0, len(larea)):
    z=larea[k]*1000
    newarea.append(z)
popden=list(df['Population Density'])
lpopden=[]
for i in range(0, len(lpop)):
    z=lpop[i]/newarea[i]
    a=int(z)
    print("POPDEN: ", a)
    lpopden.append(a)
df.drop(['Population Density'], axis=1, inplace=True)
df.insert(5, 'Population Density', lpopden)
df.sort_values(by="Road Deaths Per Million Inhabitants", inplace=True)
fig, ax=plt.subplots(figsize=(10, 8))
ax.barh(df['Country'], df['Road Deaths Per Million Inhabitants'])
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.xaxis.set_tick_params(pad=20)
ax.yaxis.set_tick_params(pad=5)
ax.grid(b=True, color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)
ax.invert_yaxis()
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize=12, color='black')
ax.set_title('Road Deaths in every Country', loc='center')
plt.show()
df.to_csv(r'C:/Users/Joel Mammen/Desktop/Datopian/CSVs/Datopian.csv')
#print(df.info())
print(df)
