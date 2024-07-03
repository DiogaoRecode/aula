"""
TRABALHANDO COM A BIBLIOTECA FAKER pelo comando no terminal: 
pip install Faker
"""

from faker import Faker
import random

faker = Faker('pt_BR')

persona = {
  "nome" : faker.name(),
  "data" : faker.date_of_birth(),
  "idade" : faker.random_int(min=18,max=18)
}


print(persona)

