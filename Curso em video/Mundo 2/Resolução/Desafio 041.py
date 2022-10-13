from datetime import date

atual = date.today().year #Pegando ano atual

nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print('\nO atleta tem {} anos'.format(idade))

if idade <=9:
  print('Classificação: MÍRIM')
elif idade <= 14:
  print('Classificação: INFANTIL')
elif idade <= 19:
  print('Classificação: JUNIOR')
elif idade <= 25:
  print('Classificação: SENIOR')
else:
  print('Classificação: MASTER')
