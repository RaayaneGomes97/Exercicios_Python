# 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Alguns métodos de resolver desse execício:


# MÉTODO 001 -- Importando da biblioteca math SOMENTE a função trunc.

from math import trunc

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))  #Repare que foi preciso retirar a refêrencia do trunc.



#
# MÉTODO 002 -- Importando a biblioteca math COM TODAS SUAS FUNCIONALIDADES.
# import math
#
# num = float(input('Digite um número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))  #Importando a função Trunc na varíavel.
#
#
#
#
# MÉTODO 003 -- SEM importar a biblioteca math.
#
# num = float(input('Digite um número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))  #Importando a função Trunc na varíavel.
#
