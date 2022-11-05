'''1. Faça um programa que leia 5 números e informe a soma e a média dos números.'''


def cont():
    soma = 0
    for i in range(1, 6):
        num = int(input("Digite um número: "))
        soma += num
    media = soma / i
    print(f"A soma dos números digitados é: {soma}\nA média dos números digitados é: {media}")

    pass

cont()