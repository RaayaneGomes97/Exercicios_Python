# 4- Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.



n = input("Digite algo: ") #Entrada de dados


print("O tipo primitivo desse valor é ", type(n))
print("Só tem espaços?", n.isspace())
print("É um número?", n.isnumeric())
print("É um número decimal?", n.isdecimal())
print('É alfabético?', n.isalpha())
print("Está em maiusculo?", n.isupper())
print("Está em minusculo?", n.islower())
