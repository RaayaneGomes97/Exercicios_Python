contM = contF = 0 #Contagem de pessoas correspondente a cada sexo
p18 = 0 #Pessoas com mais de 18 anos
girl20 = 0

while True:
  print(' Insira os dados')
  idade = int(input('\nIdade: '))
  sexo =  str(input('Sexo [F/M]: ')).strip().upper()[0]
  resp =  str(input('Deseja continuar [S/N]? ')).strip().upper()[0]

  print('\n')

  #Contabilizando homens
  if sexo == 'M':
    contM += 1

  #Contabilizando mulheres
  if sexo == 'F':
    contF += 1

  #mulheres maiores de 18
  if idade >= 18:
    p18 += 1
  #Identificando maior e a menor idade

  if sexo == 'F' and idade < 20:
    girl20 += 1

  #SAIDA DO LOOPING WHILE
  if resp == 'N':
    break

print('\nAo todo temos {} homens e {} mulheres cadastrados'.format(contM, contF))
print('Total de pessoas com mais de 18 anos: {}'.format(p18))
print('Total de mulheres com menos de 20 anos: {}'.format(girl20))
