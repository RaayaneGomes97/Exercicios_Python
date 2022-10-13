# Exercicio 31

distancia = float(input('Qual distância da viagem em km/h? '))

if distancia < 200:
  print('\nViagem até 200km... ')
  valor = distancia*0.50
  print('Valor a pagar: R$ {:.2f}'.format(valor)) # Usar apenas virgulas

else:
  print('\nViagem superiores a 200km... ')
  valor = distancia*0.45
  print('Valor a pagar: R$ {:.2f}'.format(valor))
