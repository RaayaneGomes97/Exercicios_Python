#Crie um prgorama que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

n = int(input('Digite o número: '))
cont = 0 
soma = 0
while n != 999:
  n = int(input('Digite o número: '))
  cont += 1
  soma = soma + n

print('\nVocê deu entrada em um total de {} números'.format(cont))
print('Resultado da soma de todos eles: {}'.format(soma-999))
