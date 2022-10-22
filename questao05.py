'''5. Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Faça um programa que receba a altura e o sexo de uma pessoa, após isso calcule
e imprima o seu peso ideal, utilizando as seguintes fórmulas:
• Para homens: (72,7 * A) – 58
• Para mulheres: (62,1 * A) – 44,7
Em que: A = Altura'''

print("Escolhao seu sexo:\n1 - para Feminino\n2 - para Masculino\n")
sexo = int(input("Opção digitada: "))

if sexo == 1:
    altura = float(input("\nDigite a sua altura: "))
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f}".format(peso_ideal))
elif sexo == 2:
        altura = float(input("\nDigite a sua altura: "))
        peso_ideal = (72.7 * altura) - 58
        print("Seu peso ideal é {:.2f}".format(peso_ideal))
else:
    print("\nOpção Inválida")