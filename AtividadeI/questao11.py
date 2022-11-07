'''11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 

a) o produto do dobro do primeiro com metade do segundo . 
b) a soma do triplo do primeiro com o terceiro. 
c) o terceiro elevado ao cubo.'''

n1 = int(input("Digite um número inteiro: ")) 
n2 = int(input("Digite outro número inteiro: ")) 
n3 = float(input("Digite um número real: ")) 
print(f"O produto do dobro do primeiro com metade do segundo: {(2 * n1) + (n2 / 2)}") 
print(f"\nA soma do triplo do primeiro com o terceiro: {(3 * n1) + n3}") 
print(f"\nO terceiro elevado ao cubo: {n3 ** 3}")