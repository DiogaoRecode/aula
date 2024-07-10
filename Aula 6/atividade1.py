import requests

nome_cep_integrantes = {
  "Diogo":"30110001",
  "Rodrigo":"93800156",
  "Julia":"03206020",
  "George": "40010000",
  "Isadora": "40010000"
}

for nome, cep in nome_cep_integrantes.items():
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json")
  formato = response.json()
  print(f"{nome} reside em {formato['localidade']}")

