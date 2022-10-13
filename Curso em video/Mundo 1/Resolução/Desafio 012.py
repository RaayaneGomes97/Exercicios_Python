#12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Informe o preço do produto: R$ '))
desc = p - (p*0.05)

print('\nVocê acabou de ganhar um cupom de 5% de desconto')
print('Valor a pagar: R$ {}'.format(desc))
