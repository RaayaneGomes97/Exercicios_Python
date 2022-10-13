#26 -  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('-'*30)
frase = str(input('Digite uma frase: '))
frase = frase.upper() #Removendo espaços desnecessarios
frase = frase.strip() #Removendo espaços desnecessarios

print('A letra A aparece {} vezes na frase'      .format(frase.count('A')))  # contando quantos a existem na frase
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #
print('A ultima letra A apareceu na posição {}'  .format(frase.rfind('A')+1))

print('-'*30)

print('Lembrando que o espaço entre as palavras também está sendo contablizado')
