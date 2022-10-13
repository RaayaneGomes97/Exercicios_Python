#13- Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento

print('Você acabou de ser promovido e recebeu 15% de aumento salarial!')
salario = float(input('Informe o seu salário antigo: R$ '))
aumento = salario + (salario*0.15)

print('O seu novo salário será de R$ {}' .format(aumento))
