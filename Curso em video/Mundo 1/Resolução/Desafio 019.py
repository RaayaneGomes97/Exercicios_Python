# 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# O uso de str não é obrigatório
# Porém deixaremos explicito que usaremos string
from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: ' ))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '  ))

lista = [a1, a2, a3, a4] #Lista em python
escolhido = choice(lista) #Random.choice = Método que retorna um valor de uma lista.

print('\nO aluno escolhido foi {}'.format(escolhido))
