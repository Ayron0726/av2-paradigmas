from time import sleep
import sys
import os

clear = lambda: os.system("clear")

def core():
    clear()
    print(30 * '-', 'Menu', 30 * '-')
    print(f'Selecione uma lista abaixo:\n'
          f'1 -lista 1: Fundamentos do python\n'
          f'2 -lista 2: Estruturas condicionais\n'
          f'3 -lista 3: Estruturas de repetição\n'
          f'4 -sair')
    escolha = int(input("Opção selecionada: "))

    if (escolha == 1):
        listaI()
    elif (escolha == 2):
        listaII()
    elif (escolha == 3):
        listaIII()
    elif (escolha == 4):
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
        print(30 * '-', 'ListaI - Questão:18', 30 * '-')
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

    def questao02():
        clear()
        print(30 * '-', 'ListaI - Questão:13', 30 * '-')
        print(f"Tendo como dado de entrada a altura (h) de uma pessoa\n"
                "construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:\n"
                "a) Para homens: (72.7*h) - 58\n"
                "b) Para mulheres: (62.1*h) - 44.7\n")
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
        else: 
            print("\nOpção inválida, execute novamente.\n")
     
        print('Voltando ao menu...')
        sleep(5)
        core()
        pass

    clear()
    print(30 * "-", "ListaI", 30 * "-")
    print(f"Selecione uma opção:\n"
          f"1 -Questão 01:\n"
          f"2 -Questão 02:\n"
          f"3 -Voltar ao menu:")
    escolha = int(input("Questão Selecionada: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    else:
        print("Opção inválida! Tente novamente!")
        sleep(3)
        listaI()
    pass

def listaII():
    def questao01():
        clear()
        print(30 * "-", "ListaII-Questão:06", 30 * "-")
        print(f"Faça um programa que leia o destino do passageiro, se a viagem inclui retorno\n"
                "(idae volta) e informe o preço da passagem conforme a tabela a seguir:\n"
                "Cód. Destino: 1, Destino: Região Norte, Ida: 500.00, Ida e Volta: 900.00\n"
                "Cód. Destino: 2, Destino: Região Nordeste, Ida: 350.00, Ida e Volta: 650.00\n"
                "Cód. Destino: 3, Destino: Região Centro-oeste, Ida: 350.00, Ida e Volta: 600.00\n"
                "Cód. Destino: 4, Destino: Região Norte, Ida: 300.00, Ida e Volta: 550.00)\n")
        print("Escolha o destino da viagem:\n1 - Região Norte\n2 - Região Nordeste\n3 - Região Centro-oeste\n4 - Região Sul\n")
        cod_destino = int(input("Opção escolhida: "))

        print("\nEscolha o tipo da viagem:\n1 - Só ida\n2 - Ida e volta\n")
        opcao = int(input("Opção escolhida: "))
        valor_passagem = 0

        if cod_destino == 1 and opcao == 1:
            valor_passagem = 500.00
        elif cod_destino == 1 and opcao == 2:
            valor_passagem = 900.00
        elif cod_destino == 2 and opcao == 1:
            valor_passagem = 350.00
        elif cod_destino == 2 and opcao == 2:
            valor_passagem = 650.00
        elif cod_destino == 3 and opcao == 1:
            valor_passagem = 350.00
        elif cod_destino == 3 and opcao == 2:
            valor_passagem = 600.00
        elif cod_destino == 4 and opcao == 1:
            valor_passagem = 300.00
        elif cod_destino == 4 and opcao == 2:
            valor_passagem = 550.00
        else:
            print("\nOpção inválida")
        print("O valor da sua passagem será de R${:.2f}".format(valor_passagem))
        
        print('Voltando ao menu...')
        sleep(3)
        core()
        pass

    def questao02():
        clear()
        print(30 * "-", "ListaII-Questão:07", 30 * "-")
        print(f"Escreva um programa que leia um peso na Terra e o número de um planeta e\n"
                "imprima o valor correspondente do peso neste planeta. A relação de planetas é\n"
                "dada a seguir juntamente com o valor das gravidades relativas à Terra.\n"
                "Para calcular o peso no planeta use a fórmula:"
                "Em que:\n"
                "PP = Peso no planeta\n"
                "PT = Peso na Terra\n"
                "G = Gravidade relativa\n")
        peso_terra = float(input("Digite seu peso: "))
        print("Escolha um planeta:\n1 - Mercúrio\n2 - Vênus\n3 - Marte\n4 - Júpiter\n5 - Saturno\n6 - Urano")
        esc_planeta = int(input("Opção escolhida: "))
        planeta = ""
        peso_planeta = 0

        if esc_planeta == 1:
            planeta = "Mercúrio"
            peso_planeta = (peso_terra / 10) * 0.37
        elif esc_planeta == 2:
            planeta = "Vênus"
            peso_planeta = (peso_terra / 10) * 0.88
        elif esc_planeta == 3:
            planeta = "Marte"
            peso_planeta = (peso_terra / 10) * 0.38
        elif esc_planeta == 4:
            planeta = "Júpiter"
            peso_planeta = (peso_terra / 10) * 2.64
        elif esc_planeta == 5:
            planeta = "Saturno"
            peso_planeta = (peso_terra / 10) * 1.15
        elif esc_planeta == 6:
            planeta = "Urano"
            peso_planeta = (peso_terra / 10) * 1.17
        else:
            print("Opção inválida")
        print("O seu peso no planeta {} é de {:.2f}Kg".format(planeta, peso_planeta))
        
        print('Voltando ao menu...')
        sleep(3)
        core()
        pass

    clear()
    print(30 * "-", "ListaII", 30 * "-")
    print(f"Selecione uma opção:\n"
          f"1 -Questão 01:\n"
          f"2 -Questão 02:\n"
          f"3 -Voltar ao menu:")
    escolha = int(input("Questão Selecionada: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    else:
        print("Opção inválida! Tente novamente!")
        sleep(3)
        listaII()
    pass

def listaIII():
    def questao01():
        clear()
        print(30 * "-", "ListaIII-Questão:08", 30 * "-")
        print(f"Faça um programa que leia 10 números positivos e imprima o quadrado de cada número.\n" 
                "Para cada entrada de dados deverá haver um trecho de validação para que um número\n"
                "negativo não seja aceito pelo programa.\n")
    
        for i in range(1, 11):
            num = int(input("Digite um número: "))
            if num >= 0:
                quadrado = num ** 2
                print(f"O quadrado de {num} é : {quadrado}")
            else:
                print("\nNúmero negativo, tente novamente.\n")
                break

        print('Voltando ao menu...')
        sleep(3)
        core()
        pass

    def questao02():
        clear()
        print(30 * "-", "ListaIII-Questão:10", 30 * "-")
        print(f"Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as\n"
                "caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200\n"
                "volumes, assim, esta transportadora precisa controlar a quantidade e o peso dos\n"
                "volumes para acomodar nos caminhões. Faça um programa que leia n caixas e\n"
                "seu peso, ao final, o programa deve imprimir a quantidade de volumes, o peso total\n"
                "dos volumes e o peso médio dos volumes.\n")
        import sys
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

        print('Voltando ao menu...')
        sleep(3)
        core()
        pass

    clear()
    print(30 * "-", "ListaIII", 30 * "-")
    print(f"Selecione uma opção:\n"
          f"1 -Questão 01:\n"
          f"2 -Questão 02:\n"
          f"3 -Voltar ao menu:")
    escolha = int(input("Questão Selecionada: "))

    if (escolha == 1):
        questao01()
    elif (escolha == 2):
        questao02()
    elif (escolha == 3):
        core()
    else:
        print("Opção inválida! Tente novamente!")
        sleep(3)
        listaIII()
    pass

core()