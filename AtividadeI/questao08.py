#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Digite quanto você ganha por hora: ")) 
horaTrab = float(input("Digite quantas horas você trabalhou este mês: ")) 
total = horaTrab * valorHora 
print(f"Você receberá R${total}")