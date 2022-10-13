soma = 0 
media = 0
contM = 0 
contF = 0
maior = 0
menor = 0
nomeM = ''

for x in range(1,5):
  print('===== {} pessoa ====='.format(x))
  nome  = str(input('Nome: ')).strip().capitalize()
  sexo  = str(input('Sexo [F/M]: ')).strip().upper()
  idade = int(input('Idade: '))
  print('\n')

  soma += idade # Mesma coisa que soma = soma + idade
  media = soma/4

  if sexo == 'M':'
    contM += 1
    nomeM = nome
    maior = idade
    menor = idade

    if maior > menor:
      maior = idade
    else:
      menor = idade

  if sexo == 'F':
    contF += 1

print('='*21)

print('\nA média do grupo é de {} anos '.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomeM))
print('Ao todo são {} mulheres e {} homens'.format(contF,contM))
