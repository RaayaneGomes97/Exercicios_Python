# Desafio 35

print('-'*30)
print('Analisando de triângulos')
print('-'*30)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('\nOs segmentos podem formar um triângulo!')
else:
  print('\nOs segmentos acima NÃO PODEM formar um triângulo')
