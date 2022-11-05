'''7. Faça um programa que realize a soma de todos os valores inteiros de 1 a n, sendo
que n deve ser informado pelo usuário.'''

def somatorio():
    soma = 0
    n = int(input("Digite quanto números você pretende somar: "))
    for i in range(1, n + 1):
        soma += i
    print(f"A soma dos números é: {soma}")
    pass

somatorio()