import requests
from faker import Faker

ENDPOINT='https://desafiopython.jogajuntoinstituto.org/api/users'
FORMATO_RETORNO_API='/json/'

fake = Faker('pt_BR')

nome = fake.name()
email = fake.email()
password= fake.password()

persona = {
    'nome': nome,
    'password': password,
    'email': email
}

response = requests.post(ENDPOINT + FORMATO_RETORNO_API, json=persona)
print(response.json())




