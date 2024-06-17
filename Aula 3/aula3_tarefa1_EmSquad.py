#Fazer um programa que some 4 notas e, no final tenha a media aritmetica das suas notas

aluno = str(input("Digite o seu nome: "))
print(f"{aluno},por favor informe os valores das 4 notas abaixo:")
nota1 = float(input("Digite a nota da primeira prova:"))
nota2 = float(input("Digite a nota da segunda prova:"))
nota3 = float(input("Digite a nota da terceira prova:"))
nota4 = float(input("Digite a nota da quarta prova:"))
media= (nota1+nota2+nota3+nota4)/4
print(f"Caro {aluno}, o valor da média das suas provas foi {media:.2f}")