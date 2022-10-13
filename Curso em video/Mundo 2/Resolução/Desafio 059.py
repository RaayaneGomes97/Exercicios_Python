
from time import sleep

print('=' * 30 )

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor:  '))
opc = 0

while opc != 5:
  print('''
  [ 1 ] Somar
  [ 2 ] Multiplicar
  [ 3 ] Maior 
  [ 4 ] Novos números
  [ 5 ] Encerrar programa
  ''')

  opc = int(input('\nQual é a sua opção: '))

  if opc == 1:
    soma = n1+n2
    print('A soma de {} com {} é igual a {}'.format(n1,n2,soma))

  elif opc == 2:
    mult = n1*n2
    print('\nA multiplicação de {} com {} é igual a {}'.format(n1,n2,mult))

  elif opc == 3:
    if n1 > n2:
      maior = n1
    else:
      maior = n2
    print('\nEntre {} e {} o maior é {}'.format(n1,n2,maior))
    
  elif opc == 4:
    n1 = int(input('\nPrimeiro valor: '))
    n2 = int(input('\nSegundo valor:  '))
    
  elif opc == 5:
    print('\nPrograma finalizado!')

  print('=' * 30 )

  sleep(3)
