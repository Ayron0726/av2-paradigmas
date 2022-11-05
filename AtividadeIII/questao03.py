'''3. Faça um programa que leia "n" valores. O programa deve inicialmente solicitar ao
usuário que informe a quantidade desejada de valores a ser informada, depois ler
os "n" valores e ao final imprimir a média aritmética dos valores lidos.'''
def cont():
    qtd = int(input("Digite a quantidade de dados a serem inseridos: "))
    soma = 0
    for i in range(1, qtd+1):
        num = int(input("Digite um número: "))
        soma += num
    media = soma / i
    print(f"A média aritmética dos números digitados é: {media:.2f}")
    pass

cont()