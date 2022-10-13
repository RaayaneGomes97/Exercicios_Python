# 22 -  Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: '))

maiusculo = nome.upper()
minusculo = nome.lower()
qtdnome   = len(nome)
dividido  = nome.split()

print('Analisando o seu nome...\n')

print('Seu nome em maiusculo é {}' .format(maiusculo))
print('Seu nome em minusculo é {}' .format(minusculo))
print('Seu nome completo posRsui {} letras'.format(qtdnome))
print('Seu primeiro nome é {} e possui {} letras'.format(dividido[0],len(dividido[0])))
print('Seu segundo  nome é {} e possui {} letras'.format(dividido[1],len(dividido[1])))
print('Seu ultimo   nome é {} e possui {} letras'.format(dividido[2],len(dividido[2]) ))
