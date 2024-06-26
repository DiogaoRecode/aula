
#Criacao de uma tupla com 5 nomes
tupla_alunos = ("Diogo","Diego","Douglas","Thais","Jovana")

#Convertendo tupla em lista
lista_alunos = list(tupla_alunos)
print(type(lista_alunos))
print(lista_alunos)

#Adicionando 2 itens na lista
lista_alunos.append("Carol")
lista_alunos.append("Raquel")
print(lista_alunos)

#Removendo 1 item da lista
lista_alunos.pop(0)
print(lista_alunos)

#Removendo ultimo item da lista
lista_alunos.remove("Raquel")
print(lista_alunos)
"ou outra forma de remover o ultimo"
lista_alunos.pop()
print(lista_alunos)

#Crie um dicionario com nome, idade, profissao
aluno_1 =  {"nome":"Diogo","idade":20,"profissao":"estudante"}
aluno_2 =  {"nome":"Diego","idade":35,"profissao":"medico"}

#Exiba apenas o nome do aluno 1 e a profissao do aluno 2
nome= aluno_1["nome"]
print(nome)

profi= aluno_2["profissao"]
print(profi)



