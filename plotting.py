import sys
import plotly.express as px
import plotly.offline as po
import pandas as pd

df = pd.read_csv(sys.argv[1], sep='\t') 

#featspertoken = analytic/synthetic = more features per token is more synthetic
#analysesperlength = fusional/agglutinating = features/character ≈ features/morpheme — fewer features per morpheme = more agglutinating
#analysespertypes = ambiguity
# forms per lemma?

fig3d = px.scatter_3d(df, z='featspertokens', y='featsperlength', x='analysespertypes', text='lang', opacity=0.7, labels={
    "featspertokens": "analytic / synthetic (feat/tok)",
    "featsperlength": "agglutinating / fusional (feat/char≈feat/morph)",
    "analysespertypes": "ambiguity (feat/type)"
})

fig2d = px.scatter(df, y='featspertokens', x='featsperlength', text='lang', opacity=0.7, labels={
    "featspertokens": "analytic / synthetic (feat/tok)",
    "featsperlength": "agglutinating / fusional (feat/char≈feat/morph)",
})


# tight layout
#fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

fig2d.update_layout(
    font=dict(
        size=18,
    )
)

fig3d.update_layout(
    font=dict(
        size=18,
    )
)

#fig.show()
po.plot(fig2d, filename = '2d.html', auto_open=False)
po.plot(fig3d, filename = '3d.html', auto_open=False)

