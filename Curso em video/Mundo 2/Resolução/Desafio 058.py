from random import randint

print('Estou pensando em um número entre 0 e 10')
print('Você consegue adivinhar qual é?' )
comput = randint(1,10)

loop = True # O loop está ligado
tentativas = 0


while loop == True:

  user = int(input('\nDigite um numero: '))
  tentativas +=1


  if user == comput:
    loop = False #Quando usuário acertar o loop para
  else:
    if user < comput:
      print('Mais... Tente mais uma vez')
    elif user > comput:
      print('\nMenos... Tente mais uma vez')


print('\nParabéns, você acertou com {} tentativas!'.format(tentativas))
