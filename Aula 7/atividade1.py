"""
Necessário instalar a biblioteca REQUESTS no código com o comando abaixo no terminal:
pip install requests
"""
import requests

cep = 40000000
link = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(link)

print(requisicao)

##O RESULTADO VEM EM FORMA DE DICIONARIO
dic_requisicao = requisicao.json()
uf= dic_requisicao['uf']
cidade = dic_requisicao['localidade']
bairro = dic_requisicao['bairro']

print(dic_requisicao)
print(uf)
print(cidade)
print(bairro)