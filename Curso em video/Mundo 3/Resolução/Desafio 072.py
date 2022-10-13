numeros = ('um', 'dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezenove','vinte')

while True: #Looping infinito

  opc = int(input('\nInforme um número: '))
  print('Você digitou o número {}'.format(numeros[opc-1])) # -1 pois o indice começa no zero
  
  if 0 <= opc <= 20:
    break;
