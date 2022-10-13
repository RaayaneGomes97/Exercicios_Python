# Exercicio 29

velocidade = float(input('Informe a velocidade do carro: '))
multa = (velocidade-80)*7 

if velocidade > 80:
    print('\nVocê ultrapassou o limite de de 80 km e foi mutado!')
    print( 'Valor a pagar: R$ {}'.format(multa))
else:
    print('nVocê está em velocidade compativel com a via')
