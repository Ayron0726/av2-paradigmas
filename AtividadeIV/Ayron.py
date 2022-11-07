from time import sleep
import sys
import os

clear = lambda: os.system("clear")  #função limpa tela

def core():
    clear()
    print(30 * '=', 'Menu', 30 * '=')
    print(f'Selecione uma lista abaixo:\n'
          f'1 -lista 1: Fundamentos do python\n'
          f'2 -lista 2: Estruturas condicionais\n'
          f'3 -lista 3: Estruturas de repetição\n'
          f'4 -sair')
    escolha = int(input("Opção selecionada: "))

    if (escolha == '1'):
        listaI()
    elif (escolha == '2'):
        listaII()
    elif (escolha == '3'):
        listaIII()
    elif (escolha == '4'):
        sair = str(input('Deseja sair? (s/n)'))
        if (sair == 's'):
            sys.exit()
        else:
            core()
    else:
        print("Opção inválida! Tente novamente")
        sleep(1.5)
        clear()
        core()
    pass

def listaI():
    def questao01():
        clear()
        print(30 * '=', 'ListaI - Questão:18', 30 * '=')
        print(f"Faça um programa que peça o tamanho de um arquivo para download (em MB)\n" 
            "e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de\n" 
            "download do arquivo usando este link (em minutos).\n")
        tamanho = float(input('Tamanho do arquivo(MB):')) 
        velocidade = float(input('Velociade (MBps):')) 
        velocidade_minuto = float(velocidade*60) 
        print('Tempo aproximado:', tamanho/velocidade_minuto)
        print("Voltando ao menu")
        sleep(3)
        core()
        pass
    