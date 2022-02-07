import pandas as pd
import plotly.express as px
import csv

df=pd.read_csv('data.csv')
mean=df.groupby(['id','level'],as_index=False)['attempt'].mean()
graph=px.scatter(mean,x='id',y='level',color='attempt',size='attempt')
graph.show()