'''13. Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 

a) Para homens: (72.7*h) - 58 
b) Para mulheres: (62.1*h) - 44.7'''

print("Escolha o seu gênero:") 
print("\n1-Masculino\n2-Feminino\n") 
genero = int(input()) 
if genero == 1: 
    altura = float(input("\nDigite sua altura: ")) 
    peso = (72.7 * altura) - 58 
    print(f"Seu peso ideal é: {peso:.2f}Kg") 
elif genero == 2: 
    altura = float(input("\nDigite sua altura: ")) 
    peso = (62.1 * altura) - 44.7 
    print(f"Seu peso ideal é: {peso:.2f}Kg") 
else: print("\nOpção inválida, execute novamente.\n")