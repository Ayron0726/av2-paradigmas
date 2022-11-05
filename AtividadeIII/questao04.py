'''4. Faça um programa que imprima todos os valores entre 0 e 100 múltiplos de 10.'''

def multiplos():

    for i in range(1, 101):
        if i % 10 == 0:
            print(f"Números múltiplos de 10: {i}\n")

    pass

multiplos()

    
    