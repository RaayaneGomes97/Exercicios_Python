#24 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu? '))

#Fazendo atribuições para verificar depois.

cidade = cidade.strip() # Removendo todos espaços inuteis (esquerda e direita)
cidade = cidade.upper() # Colocando todos os caracteres em maiusculo.

print('-'*40)
print(cidade[:5] == 'SANTO') #Santos tem 4 caracteres por isso [:5]. Iremos verificar apenas ele.
