def contar_vogais(palavra):
  vogais = "AEIOU"
  contador = 0
  
  for letra in palavra:
    if letra in vogais:
      contador += 1  
  return contador

palavra = str(input("Digite uma palavra: "))
texto_maiusculas = palavra.upper()
print(f"Número de vogais: {contar_vogais(texto_maiusculas)}")