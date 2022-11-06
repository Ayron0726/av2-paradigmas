'''10.Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as
caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200
volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos
volumes para acomodar nos caminhões. Faça um programa que leia n caixas e
seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso total
dos volumes e o peso médio dos volumes.'''

import sys
def caixas():
    qtdCaixas = int(input("Digite a quantidade de caixas: "))
    pesoTotal = 0
    for i in range(1, qtdCaixas + 1):
        if (qtdCaixas <= 200):
            peso = float(input(f"Digite o peso da caixa {i}: "))
            pesoTotal += peso
        elif (qtdCaixas > 200):
            print("Limite de volumes excedido")
            sys.exit()
        if (pesoTotal > 10000):
            print("Limite de peso excedido")
            sys.exit()
    print(f"Total de volumes: {qtdCaixas}\nPeso total da carga: {pesoTotal:.2f}Kg")
    pesoMedio = pesoTotal / qtdCaixas
    print(f"\nPeso médio da carga: {pesoMedio:.2f}Kg\n")

    pass

caixas()