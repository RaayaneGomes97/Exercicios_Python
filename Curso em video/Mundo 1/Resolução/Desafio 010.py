# 10. Faça um algoritmo que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ele poderá comprar.
# Considere o valor do dollar  U$ 1.00 = R$ 5.62


real = float(input('Quanto você deseja trocar? R$ '))
# Cuidado para não utilizar vírgulas.
# Os valores em ponto flutuante nos python são representados com PONTO . 

dolar = real / 5.62
euro = real / 6.63
libra = real / 7.36

print('-'*50)

print('Com R$ {:.2f} você consegue trocar por US$ {:.2f}'.format(real, dolar))
print('Com R$ {:.2f} você consegue trocar por  €  {:.2f}'.format(real, euro))
print('com R$ {:.2f} você consegue trocar por  £  {:.2f}'.format(real, libra))

print('-'*50)
