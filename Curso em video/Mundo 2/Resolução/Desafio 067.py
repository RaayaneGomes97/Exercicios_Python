soma = 0

while True: #Looping infinito
  print('-'*40)

  n = int(input('Digite o valor da tabuada: '))
  
  print('\n')

  if n < 0:
    break;


  for x in range(1,11):
    print('{} x {} = {}'.format(n, x, n*x))

  
print('Programa encerrado!')
