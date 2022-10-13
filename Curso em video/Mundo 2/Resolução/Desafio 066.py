soma = 0

while True: #Looping infinito
  num = int(input('Digite um valor: '))

  if num == 999: 
    break #Interrompendo fluxo do laço
  soma += num
print('\nA soma dos valores é {}!'.format(soma))
print('Fim!')
