import plotly.express as px
import pandas as pd

df = pd.read_csv("data.tsv", sep='\t') 

fig = px.scatter_3d(df, x='featspertokens', y='analysesperlength', z='analysespertypes', text='lang', opacity=0.7)

# tight layout
#fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

fig.show()
