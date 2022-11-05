'''3. Faça um programa que receba um número inteiro e verifique se este número é
maior que 20, em caso afirmativo o programa deverá multiplicar o valor por 2 e em
caso negativo deve multiplicar por 4. Após realizar o cálculo o programa deve
imprimir a mensagem: "Resultado: <valor do resultado>", em que <valor do
resultado> deve ser substituído pelo resultado do cálculo.'''

numero = int(input("Digite u número: "))

if numero > 20:
    numero = numero * 2
    print("Resultado: {}".format(numero))
else:
    numero = numero * 4
    print("Resultado: {}".format(numero))