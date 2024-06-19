
valor = float((input("Digite o valor total da compra: ")))

if (valor > 500):
  valorDesconto = valor*(30/100)
  print(f"PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%, VOCÊ GANHOU O VALOR DE: R$ {valorDesconto:.2f}" )
elif (valor>= 250):
  valorDesconto = valor*(10/100)
  print(f"PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00, VOCÊ GANHOU O VALOR DE: R$ {valorDesconto:.2f}")
else:
  print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")