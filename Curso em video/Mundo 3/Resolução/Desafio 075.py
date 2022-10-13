pares = 0

num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))

print(f'\nVocê digitou os valores: {num}')

print('-'*40)
if 9 in num:
    print(f'\nO valor 9 apareceu {num.count(9)} veze(s).')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')

print(f'Foram digitados os seguintes valores pares: ', end='')
for n in num:
  if n % 2 == 0:
      pares = num

print(pares)
