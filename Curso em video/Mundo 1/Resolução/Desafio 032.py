# Exercicio 32

ano = int(input('Informe o ano: '))

if (ano % 4 == 0): # Um ano bissexto é divisível por 4, portanto...
  print('{} é um ano bissexto!'.format(ano))
else:
  print('{} NÃO é um ano bissexto!'.format(ano))
