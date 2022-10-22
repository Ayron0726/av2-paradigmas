'''4. Um escritório de contabilidade, está realizando o reajuste do salário dos
funcionários de todos os seus clientes. Para isso, estão utilizando como referência
o reajuste acordado com os sindicatos de cada classe trabalhadora, conforme
apresentado na tabela a seguir. Para ajudar o escritório nesta tarefa, faça um
programa que receba o salário atual, o cargo conforme especificado na tabela a
seguir e realize o cálculo do reajuste do salário. Ao término do cálculo o programa
deve imprimir o valor do reajuste e o novo salário do funcionário.

cód cargo: 1, cargo: Auxiliar de escritório, % reajuste acordado: 7%
cód cargo: 2, cargo: Secretário(a), % reajuste acordado: 9%
cód cargo: 3, cargo: Cozinheiro(a), % reajuste acordado: 5%
cód cargo: 4, cargo: Entregador(a), % reajuste acordado: 12%'''

print("Escolha uma das opções abaixo para o seu cargo:")
print("\n1 - Auxiliar de escritório\n2 - Secretátio(a)\n3 - Cozinheiro(a)\n4 - Entregador(a)\n")
opcao = int(input("Opção escolhida: "))
salario = 0
novo_salario = 0

if opcao == 1:
    salario = float(input("Digite o seu salário em R$: "))
    novo_salario = ((salario * 7) / 100) + salario
    print("Seu salário de R${:.2f} com reajuste de 7% passará a ser R${:.2f}".format(salario, novo_salario))
elif opcao == 2:
    salario = float(input("Digite o seu salário em R$: "))
    novo_salario = ((salario * 9) / 100) + salario
    print("Seu salário de R${:.2f} com reajuste de 9% passará a ser R${:.2f}".format(salario, novo_salario))
elif opcao == 3:
    salario = float(input("Digite o seu salário em R$: "))
    novo_salario = ((salario * 5) / 100) + salario
    print("Seu salário de R${:.2f} com reajuste de 5% passará a ser R${:.2f}".format(salario, novo_salario))
elif opcao == 4:
    salario = float(input("Digite o seu salário em R$: "))
    novo_salario = ((salario * 12) / 100) + salario
    print("Seu salário de R${:.2f} com reajuste de 12% passará a ser R${:.2f}".format(salario, novo_salario))
else:
    print("Opção Inválida")
