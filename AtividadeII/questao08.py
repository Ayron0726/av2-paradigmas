'''8. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
correspondente. Caso o usuário digite um número fora desse intervalo, deverá
aparecer uma mensagem informando que não existe mês com este número.'''

num = int(input("Digite um número entre 1 e 12: "))

if num == 1:
    print("Janeiro")
elif num == 2:
    print("Fevereiro")
elif num == 3:
    print("Março")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Maio")
elif num == 6:
    print("Junho")
elif num == 7:
    print("Julho")
elif num == 8:
    print("Agosto")
elif num == 9:
    print("Setembro")
elif num == 10:
    print("Outubro")
elif num == 11:
    print("Novembro")
elif num == 12:
    print("Dezembro")
else:
    print("Não existe mês com esse número!")
                                    
                    