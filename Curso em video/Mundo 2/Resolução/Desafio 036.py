casa    = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos    = float(input('Quantos anos de financiamento? '))

parcela = casa/(anos*12) # Prestação mensal
limite = salario*0.30 #ultrapassar 30%

if parcela > limite:
  print('\nPara pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.0f}. O valor excede 30% de seu salário'.format(casa,anos,parcela)) 

  print('\n')
  print('Emprestimo NEGADO!')
else: 
  print('\nPara pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa,anos,parcela))
  print('\nEmpréstimo ACEITO!')
