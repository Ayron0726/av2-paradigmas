#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi
raio = float(input("Digite o raio de um círculo: "))
area = pi * (raio**2) 
print(f"A área do círculo é:{area:.2f}")