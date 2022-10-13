# 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Informe os dados abaixo:\n')

dias =   int(input('Quantos dias ele foi alugado: '))
km   = float(input('Quantos km foram percorrido: '))


total = (dias * 60) + (0.15 * km)

print('Total a pagar: R$ {:.2f} '.format(total))
