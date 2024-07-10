import os
import requests
import json

nome_cep_integrantes = {
  "Diogo":"30110001",
  "Rodrigo":"93800156",
  "Julia":"03206020",
  "George": "40010000",
  "Isadora": "40010000"
}

squad = {}
for nome, cep in nome_cep_integrantes.items():
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
  formato = response.json()
  print(f"{nome} mora em {formato['localidade']}")
  squad[nome] = {
    "CEP": cep,
    "CIDADE": formato['localidade'],
    "ESTADO": formato['uf'],
    "DDD": formato['ddd']
  }

os.makedirs("arquivo", exist_ok=True)
with open('arquivo/endereco_componente_squad.json', 'w') as file:
  json.dump(squad, file, ensure_ascii=True)