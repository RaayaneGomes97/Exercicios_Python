# 28 - Escreva um programa que façao  computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhidopelo computador. O programa deverá escrevetr na tela se o usuário venceu ou perdeu

#Importando biblioteca
from random import randint 
from time     import sleep 

pc = randint(0,5) #Gerando um numero aleatório de 1 a 5 e armazenando na variavel pc

print('-'*50) # Organizando código
print("Estou pensando em um número entre 0 e 5.")
print('-'*50) # Organizando código

num = int(input('Que número seria esse? ')) #resp = resposta do jogador

print('\nProcessando')
sleep(3) # Gerando um delay de 3 segundos


if num == pc:
    print('\nParabéns, você acertou!')
else:
    print('\nVocê errou! Eu estava pensando no pcero {}'.format(pc))


