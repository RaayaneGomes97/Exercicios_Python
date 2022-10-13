frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
  # print(junto[letra])
  inverso += junto[letra]

if inverso == junto:
  print('\nTemos um palíndromo!')

else:
  print("A frase digitada NÃO é um palíndromo!")
print(junto, inverso)
