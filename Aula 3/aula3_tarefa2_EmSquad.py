"""                                    ENUNCIADO
                                      ------------
Desafio: Faça um código que permita, ao inserir um valor, o retorno de 5 outputs, sendo eles:
primeiro output: deve apresentar como resultado o dobro do valor inserido;
segundo output: deve apresentar como resultado o triplo do valor inserido;
terceiro output: deve apresentar como resultado o valor inserido ao quadrado;
quarto output: deve apresentar como resultado a raiz quadrada do valor inserido;
quinto output: deve apresentar como resultado a raíz cúbica do valor inserido.
"""

numero = float(input("Vamos brinca agora!!! Por favor digite um número:"))

dobro = numero * 2
triplo = numero * 3
quad = numero * numero
raiz_quadrada = numero ** 1/2
raiz_tripla = numero ** 1/3

print (f"Você digitou o valor : {numero:.0f} ")
print (f"O dobro desse valor : {dobro:.0f} ")
print (f"O triplo desse valor : {triplo:.0f} ")
print (f"O valor desse número  ao quadrado : {quad:.0f} ")
print (f"A raiz quadrada desse valor : {raiz_quadrada:.2f} ")
print (f"A raiz tripla desse valor  : {raiz_tripla:.2f} ")



