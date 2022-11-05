'''2. Faça um programa que leia 10 valores e ao final imprima a média aritmética dos
valores lidos.'''

def cont():
    soma = 0
    for i in range(1, 11):
        num = int(input("Digite um número: "))
        soma += num
    media = soma / i
    print(f"A média aritmética dos números digitados é: {media:.2f}")

    pass

cont()
