# 0 - 1 - 1 - 2 
#    t1  t2
resp = 'S'
soma = quant = media = maior = menor = 0

#ou então while resp in 'Ss':
while resp ==  'S':
  number = int(input('\nDigite um número: '))
  resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0] #pegar só primeira letra
  
  soma += number
  quant += 1

  if quant == 1:
    maior = menor = number

  else:
    if number > menor:
      maior = number

    if number < maior:
      menor = number

media = soma/quant
print('\nVocê digitou {} números e a média foi {}'.format(quant,media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))

