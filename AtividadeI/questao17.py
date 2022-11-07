'''17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam 
R$ 25,00. -Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 
situações: -comprar apenas latas de 18 litros; -comprar apenas galões de 3,6 litros; -misturar latas e 
galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os 
valores para cima, isto é, considere latas cheias.'''

metros_cliente = float(input("Área em m²:")) 
litros = (metros_cliente / 6)*1.1 
qnt_latas = int(litros / 18) 
if (metros_cliente % 18 != 0): 
    qnt_latas += 1 
    qnt_galoes = int((litros / 3.6)) 
    if (metros_cliente % 3.6 != 0): 
        qnt_galoes += 1 
        qtd_galao_misto = int(litros/3.6) 
        qtd_lata_misto =((litros - qtd_galao_misto * 3.6) / 18) 
        valor_galao_misto = qtd_galao_misto * 25 
        valor_lata_misto = qtd_lata_misto * 80 
        print("Latas necessárias:", qnt_latas, "\tPreço: R$", qnt_latas * 80) 
        print("Galões necessários:", qnt_galoes, "\tPreço: R$", qnt_galoes * 25) 
        print('considerando o menor desperdíciode tinta, temos:') 
        print(f'quantidade galões: {qtd_galao_misto:.0f}') 
        print(f'quantidade latas: {qtd_lata_misto:.0f}') 
        print(f'quantidade total mistas: {qtd_galao_misto + qtd_lata_misto:.0f}')
        print(f'valor total considerando GALOES e LATAS é: R$ {valor_galao_misto + valor_lata_misto:.2f}')