"""
Filtre as pessoas levando em consideração os seguintes critérios:
com idade maior que 40 anos
com renda maior de 5 mil
com renda maior de 15 mil
"""


import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')

df = pd.DataFrame(data=dados)

filtro = (df['idade'] > 40) & (df['renda'] > 5000) & (df['renda'] < 15000)
resultado = df[filtro]

print(resultado)