print('Calculando seu rendimento escolar...')

print('-'*30)

n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))

media = (n1+n2)/2 #Calculando a média
print('-'*30)

print('Média: {}\n'.format(media))

if media < 5.0:
  print('REPROVADO')

if media >= 5.0 and media <= 6.9:
  print('RECUPERAÇÃO')
  
if media > 7.0:
  print('APROVADO')

