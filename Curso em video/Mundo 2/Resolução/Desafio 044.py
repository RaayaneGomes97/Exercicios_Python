# a vista: 10% de desconto
# a vista no cartao: 5% de desconto
# 2x  cartão: preço normal
# 3x ou mais no cartao: 20% de juros

preço = float(input('Preço das compras: R$ '))

print('''
[ 1 ] À vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')

opc = int(input('\nQual é a opção? '))

if opc == 1:
  preçoatual = preço - (preço*0.10)
  print('\nVocê tem direito a 10% de desconto')
  print('Sua compra de R$ {:.2f} irá custar R$ {:.2f}'.format(preço, preçoatual))

elif opc == 2:
  preçoatual = preço - (preço*0.05)
  print('\nVocê tem direito a 5% de desconto')
  print('Sua compra de R$ {:.2f} irá custar R$ {:.2f}'.format(preço, preçoatual))

elif opc == 3:
  print('\nValor a pagar: {}'.format(preço))

elif opc == 4:
  juros = preço*0.20
  preçoatual = preço + juros
  parcelas = int(input('Quantas parcelas? '))
  
  
  print('\nSua compra será parcelada em {}x com 20% de juros'.format(parcelas))
  print('Sua compra de R$ {:.2f} irá custar R$ {:.2f}'.format(preço, preçoatual))

else:
  print('\nOpção inválida. Tente novamente!')
