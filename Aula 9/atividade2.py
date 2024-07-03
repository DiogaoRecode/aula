import pandas as pd

dados = {
  "Nome": ["João","Marta","Ary","Matheus","Michelle","Diogo","Airton"],
  "Idade": [51,37,23,24,33,21,25],
  "Cidade": ["SP","BA","MA","PB","BA","BA","BA"]
}

indice=0
df = pd.DataFrame(data=dados)
print(df)

##USANDO RECURSO DE WHILE E CONCEITO DE DICIONARIO
while indice < len(df['Cidade']): 
  if (df['Cidade'][indice]=="PB"):
    nome = dados["Nome"][indice]
    idade = dados["Idade"][indice]
    cidade = dados["Cidade"][indice]
    print(f'Nome: {nome}, Idade: {idade}, Cidade: {cidade}') 
  indice +=1
  

  ##USANDO FILTRO PELO PANDAS
filtro = df[df['Cidade'] == "PB"]
print("\nUsando conceito de DataFrame filtrado :")
print(filtro)
