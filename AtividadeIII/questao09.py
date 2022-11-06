'''9. Faça um programa que permita entrar com números e imprimir o quadrado de cada
número digitado até entrar um número múltiplo de 6 que deverá ter seu quadrado
impresso também.'''

def multiplo():
    for i in range(1, 11):
        num = int(input("Digite um número: "))
        if(num % 6 != 0):
            quad = num ** 2
            print(f"\nO quadrado de {num} é: {quad}\n")
        elif(num % 6 == 0):
            quad = num ** 2
            print(f"\nO número {num} é múltiplo de 6, e o seu quadrado é: {quad}\n")
            break
    pass

multiplo()
    
