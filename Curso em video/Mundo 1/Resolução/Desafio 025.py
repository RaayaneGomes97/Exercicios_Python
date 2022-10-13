#22 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite seu nome completo: '))

#Fazendo atribuições para verificar depois.

nome = nome.strip() # Removendo todos espaços inuteis (esquerda e direita)
nome = nome.lower() # Colocando todos os caracteres em minusculo.

print('-'*40)
print('Seu nome tem silva? {} ' .format('silva' in nome)) #Santos tem 4 caracteres por isso [:5]. Iremos verificar apenas ele.
