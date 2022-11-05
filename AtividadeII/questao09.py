'''9. O banco Facimp concederá um crédito especial com juros de 2% aos seus clientes
de acordo com o saldo médio no último ano. Faça um programa que leia o saldo
médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. O
programa deve imprimir uma mensagem informando o saldo médio e o valor de
crédito.'''

def valorCredito():
    saldoMedio = float(input("Digite o seu saldo médio: R$ "))
    if saldoMedio >= 0 and saldoMedio <= 500:
        credito = 0
    elif saldoMedio > 500 and saldoMedio <= 1000:
        credito = (saldoMedio * 30) / 100
    elif saldoMedio > 1000 and saldoMedio <= 3000:
        credito = (saldoMedio * 40) / 100
    elif saldoMedio > 3000:
        credito = (saldoMedio * 50) / 100

    print(f'Seu saldo médio: R$ {saldoMedio:.2f}\nSeu valor de crédito: R$ {credito:.2f}')

    pass

valorCredito()