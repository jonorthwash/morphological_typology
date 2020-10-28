import sys
import plotly.express as px
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t') 

fig = px.scatter_3d(df, y='featspertokens', z='analysesperlength', x='analysespertypes', text='lang', opacity=0.7)

# tight layout
#fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

fig.show()
