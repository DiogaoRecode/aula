frequencia_aluno = int(input("Quantas dias vocë foi a academia?"))
resposta = input ("Teve alguma falta no meio desse tempo? (sim/não): ")

if resposta in ["sim","s","yes", "y"]:
     opcao = True
elif resposta in ["não", "nao", "n"]:
    opcao = False
else:
    print("Resposta inválida. Por favor, responda 'sim' ou 'não'.")
    opcao = False  

if frequencia_aluno == 21 and opcao:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
else:
   print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.") 
