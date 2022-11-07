'''15. Faça um Programa que pergunte quanto você ganha por hora 
e o número de horas trabalhadas no mês. Calcule e mostre o total 
do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o 
sindicato, faça um programa que nos dê: 

a) salário bruto. 
b) quanto pagou ao INSS. 
c) quanto pagou ao sindicato. 
d) o salário líquido. 
e) calcule os descontos e o salário líquido, conforme a tabela abaixo: 
+ Salário Bruto : R$ 
- IR (11%) : R$ 
- INSS (8%) : R$ 
- Sindicato ( 5%) : R$ 
= Salário Liquido : R$ 
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input("\nDigite quanto você ganha por hora: ")) 
hora_trab = float(input("Digite quantas horas você trabalhou este mês: ")) 
salario_bruto = hora_trab * valor_hora 
print(f"\n+ Salário Bruto: R${salario_bruto:.2f}") 
print(f"\n- IR(11%):R${(salario_bruto * 0.11):.2f}") 
print(f"\n- INSS(8%):R${(salario_bruto * 0.08):.2f}") 
print(f"\n- Sindicato(5%):R${(salario_bruto * 0.05):.2f}") 
print(f"\n= Salário Líquido:R${salario_bruto - (salario_bruto * 0.24):.2f}','\n")