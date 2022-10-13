import random

a1 = str(input('Primeiro aluno: ')) #Str = Deixando explicito que usaremos string
a2 = str(input('Primeiro aluno: '))
a3 = str(input('Primeiro aluno: '))
a4 = str(input('Primeiro aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista) #Embaralhar valores da lista

print('A ordem de apresentação será: ')
print(lista)

