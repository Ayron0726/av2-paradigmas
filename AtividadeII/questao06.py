'''6. Faça um programa que leia o destino do passageiro, se a viagem inclui retorno (ida
e volta) e informe o preço da passagem conforme a tabela a seguir:

Cód. Destino: 1, Destino: Região Norte, Ida: 500.00, Ida e Volta: 900.00
Cód. Destino: 2, Destino: Região Nordeste, Ida: 350.00, Ida e Volta: 650.00
Cód. Destino: 3, Destino: Região Centro-oeste, Ida: 350.00, Ida e Volta: 600.00
Cód. Destino: 4, Destino: Região Norte, Ida: 300.00, Ida e Volta: 550.00'''

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
