print('='*30)
print('NÚMERO PRIMO ')
print('='*30)

number = int(input('Digite um número: '))
cont = 0

for x in range(1,number+1):
  if(number % x == 0):
    print('\033[0:34m{}'.format(x), end =' ')
    cont += 1

  else:
    print('\033[0:31m{}'.format(x), end = ' ')


if(cont < 4):
  print('\n\n\033[mO número {} foi divisível {} vezes'.format(number,cont))
  print('E por isso ele \033[0:34mÉ PRIMO!')

else:
  print('\n\n\033[m número {} foi divisível {} vezes'.format(number,cont))
  print('E por isso ele \033[0:31mNÃO É PRIMO!')
