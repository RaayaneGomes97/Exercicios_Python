from random import randint
v = d = 0
print('-'*50)

while True:
  player = int(input('\nDigite um valor: '))
  pc = randint(1,11) #Gerando numeros aleatórios de 1 a 10
  total = player + pc
  tipo = ' '

  while tipo not in 'PI':
    tipo = str(input('Par ou impar [P/I]? ')).strip().upper()[0]

    print('\nVocê jogou {} e  computador {}. Total e {}'.format(player,pc,total))

    if tipo == 'P':
      if total % 2 == 0:
        print('Você VENCEU!') 
        v += 1 #Contabilziando valores
        break
      else: 
        print('Você perdeu!') 
        d += 1 #Contabilziando vlaores
        break


    elif tipo == 'I':
      if total % 2 != 0:
        print('Você Perdeu!') 
        v += 1 #Contabilziando valores
        break

      else: 
        print('Você VENCEU!') 
        d += 1 #Contabilziando vlaores
        break
print('FIM DE JOGOS! Você um total de {} e {} derrotas'.format(p, d))
