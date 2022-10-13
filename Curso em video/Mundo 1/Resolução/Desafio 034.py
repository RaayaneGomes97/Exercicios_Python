#Desafio 034

salario = float(input('Qual é o salário do funcionário? '))

if salario < 1250:
  reajuste = salario + salario*0.15 # Calculando um aumento de 15%
  print('Quem ganhava {} passa a ganhar {}'.format(salario, reajuste))

else:
  reajuste = salario + salario*0.10  # Calculando um aumento de 10%
  print('Quem ganhava {} passa a ganhar {}'.format(salario, reajuste))
