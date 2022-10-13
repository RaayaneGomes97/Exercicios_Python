from random import choice

print('-'*30)
print('JOKEN PO')
print('-'*30)

p1 = str('pedra')
p2 = str('papel')
p3 = str('tesoura')

lista = [p1, p2, p3]
pc = choice(lista)

print('''
1 | Pedra
2 | Papel
3 | Tesoura \n ''')

opc = int(input('Você: '))

# JOGADOR = PEDRA:
if opc == 1 and pc == 'pedra':
  print('Computador: {}'.format(pc))
  print('\nEmpate!')

if opc == 1 and pc == 'papel':
  print('Computador: {}'.format(pc))
  print('\nVocê PERDEU!')
  
if opc == 1 and pc == 'tesoura':
  print('Computador: {}'.format(pc))
  print('\nParabéns! Você VENCEU!')
#----------------

# JOGADOR = PAPEL:
if opc == 2 and pc == 'pedra':
  print('Computador: {}'.format(pc))
  print('\nParabéns! Você VENCEU!')

if opc == 2 and pc == 'papel':
  print('Computador: {}'.format(pc))
  print('\nEmpate!')
  
if opc == 2 and pc == 'tesoura':
  print('Computador: {}'.format(pc))
  print('\nVocê PERDEU!')
#----------------



# JOGADOR = tesoura:
if opc == 3 and pc == 'pedra':
  print('Computador: {}'.format(pc))
  print('\nVocê PERDEU!')

if opc == 3 and pc == 'papel':
  print('Computador: {}'.format(pc))
  print('\nParabéns! Você VENCEU!')
  
if opc == 3 and pc == 'tesoura':
  print('Computador: {}'.format(pc))
  print('\nEmpate!')
#----------------
