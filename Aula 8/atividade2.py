def separa_Time(nome:str, matricula:int)-> str:
  if matricula % 2 == 0:
    print(f"{nome}, VOCÊ ESTÁ NO TIME AZUL")
    return "Azul"
  else:
    print(f"{nome}, VOCÊ ESTÁ NO TIME AMARELO")
    return "Amarelo"

def imprimir_lista(lista_alunos):
    print("Lista de alunos com seu respectivos times:")
    for aluno in lista_alunos:
      print(f"Aluno: {aluno[0]} | Time: {aluno[2]}")

lista_alunos = []

while len(lista_alunos) < 3:
  nome = str(input("Digite o seu nome: "))
  matricula = int(input("Digite o numero da sua mátricula: "))
  time = separa_Time(nome,matricula)
  lista_alunos.append((nome,matricula,time))

print(type(lista_alunos))
imprimir_lista(lista_alunos)

