'''7. Escreva um programa que leia um peso na Terra e o número de um planeta e
imprima o valor correspondente do peso neste planeta. A relação de planetas é
dada a seguir juntamente com o valor das gravidades relativas à Terra. Para
calcular o peso no planeta use a fórmula:
Em que:
PP = Peso no planeta
PT = Peso na Terra
G = Gravidade relativa'''

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