
"""ATIVIDADE EM SQUAD"""
"""   
Leiam o caso abaixo e executem usando Python.

A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:

Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10.
"""

nome_completo = "PAULA MARTINS"
nome = "PAULA"
mes = "JANEIRO"
valor = "R$ 500,00"
desconto = 10
cupom = nome+"É"+str(desconto)


print("Olá, " + nome_completo , ". Em JANEIRO você realizou uma compra no valor de", valor , "e ganhou um desconto de", desconto ,"% em sua próxima compra. Use o cupom" , cupom )

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" 

"""CONTEUDO DA AULA"""
""" TIPO DE FORMAT PARA IMPRESSAO DE MENSAGEM"""
format_1 = f"O nome da pessoa é {nome_completo} e faz aniversario no mês de {mes}"
format_2 = "O nome da pessoa é {}, desconto dela é {}".format(nome, desconto) 
format_3 = "O nome da pessoa é {a}, desconto dela é {b}".format(a=nome, b=desconto)

print (format_1)
print (format_2)
print (format_3)

""" VERIFICAR O TIPO DE VARIAVEL"""
tipo_nome= type(nome)

print (tipo_nome)


"""INPUT - Inserindo informaçoes pela digitaçao do usuario"""

nome = str(input ("Digite o seu nome: "))
idade = int(input("Digite a sua idade: 12"))
print(type(idade))
idade_futura=idade + 3

print(f"O nome da pessoa é {nome}, sua idade hoje é {idade}. Daqui 3 anos terá {idade_futura}.")
