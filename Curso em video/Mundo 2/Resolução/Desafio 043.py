peso = float(input('Qual é o seu peso(kg)? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

print('\nO IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
  print('Você está ABAIXO do peso normal')

elif 18.5 <= imc <25:
  print('Você está no peso normal ')

elif 25 <= imc <30:
  print('Você está no peso normal ')

elif 30 <= imc <40:
  print('Você está em OBESIDADE ')

elif imc >= 40:
  print('Você está em OBESIDADE MÓRBIDA! ')

