'''10.Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as
caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200
volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos
volumes para acomodar nos caminhões. Faça um programa que leia n caixas e
seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso total
dos volumes e o peso médio dos volumes.'''

def caixas():
    pesoMedio = 0
    pesoTotal = 0
    caixaTotal = 0
    qtdCaixas = int(input("Digite a quantidade de caixas: "))
    pesoCaixa = float(input("Digite o peso das caixas: "))
    if(pesoCaixa > 0 and pesoCaixa <= 10000 and qtdCaixas > 0 and qtdCaixas <= 200 ):
        pesoTotal = qtdCaixas * pesoCaixa
        caixaTotal += qtdCaixas
        pesoMedio = pesoTotal / qtdCaixas
        print(f"Quantidade de volumes: {caixaTotal}\nPeso total dos volumes: {pesoTotal:.2f}\nPeso médio dos volumes: {pesoMedio:.2f}")  
        if(pesoTotal > 10000.00):
            print("Limite excedido de peso")
        elif(qtdCaixas > 200):
            print("Limite de volumes excedido")
    else:
        print("Valor inválido")
    pass

caixas()