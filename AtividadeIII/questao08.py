'''8. Faça um programa que leia 10 números positivos e imprima o quadrado de cada
número. Para cada entrada de dados deverá haver um trecho de validação para
que um número negativo não seja aceito pelo programa.'''

def quadrado():
    for i in range(1, 11):
        num = int(input("Digite um número: "))
        if num >= 0:
            quadrado = num ** 2
            print(f"O quadrado de {num} é : {quadrado}")
        else:
            print("\nNúmero negativo, tente novamente.\n")
            break
        pass

quadrado()