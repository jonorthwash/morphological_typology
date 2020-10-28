import sys
import plotly.express as px
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t') 

#featspertoken = analytic/synthetic = more features per token is more synthetic
#analysesperlength = fusional/agglutinating = features/character ≈ features/morpheme — fewer features per morpheme = more agglutinating
#analysespertypes = ambiguity
# forms per lemma?

#fig = px.scatter_3d(df, y='featspertokens', z='featsperlength', x='analysespertypes', text='lang', opacity=0.7, labels={
#    "featspertokens": "analytic / synthetic (feat/tok)",
#    "featsperlength": "fusional / agglutinating (feat/char≈feat/morph)",
#    "analysespertypes": "ambiguity (feat/type)"
#})

fig = px.scatter(df, y='featspertokens', x='featsperlength', text='lang', opacity=0.7, labels={
    "featspertokens": "analytic / synthetic (feat/tok)",
    "featsperlength": "agglutinating / fusional (feat/char≈feat/morph)",
})


# tight layout
#fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

fig.show()
