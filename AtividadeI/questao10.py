#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

c = float(input("Digite a temperatura em Celsius: ")) 
f = (c * 1.8) + 32 
print(f"A temperatura em Fahrenheit é: {f:.1f}")