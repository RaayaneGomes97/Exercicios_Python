#27: Faça um programa que leia o nome
# completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

print('-'*30)

nome = str(input('Digite uma frase: ')).strip() #Removendo espaços inuteis 
nome = nome.split() # Dividir cadeia criando uma indexaçao nova a elas

# Exemplo:
# Fulano cilano  Silva
# Fulano  = 0    Ciclano = 1    Silva = 3

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo   nome é {}'.format(nome[len(nome)-1]))
# len(nome) Exibe o comprimento da variavel
