'''10. Faça um programa que leia dois valores inteiros e efetue a adição. Caso o valor
somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8, caso o
valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

def calculadora():

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    soma = n1 + n2

    if soma > 20:
        soma += 8
    else:
        soma -= 5
        
    print(f"O resultado da soma é: {soma}")

    pass

calculadora()