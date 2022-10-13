idade = 0
cont = 0

for c in range(1, 7,):
  idade = int(input('Informe a idade da {} pessoa: '.format(c)))
  if idade >= 21:
    cont += 1

print('\nVocê informou a idade de 7 pessoas.')
print('Apenas {} atingiram a maioridade (21 anos)'.format(cont))
