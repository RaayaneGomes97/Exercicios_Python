from time import sleep #Importando sleep
num = int(input('Informe um número: '))

print('-'*30) # ------------- ...

opc = int(input(
'''
| 1 | Para binário
| 2 | Para octa
| 3 | Para hexadecimal

Informe a opção desejada: '''))

print('-'*30)  # ------------- ...
print('Processando...')
print('-'*30)  # ------------- ...


sleep(3) #Aguardar 3 segundos

if opc == 1:
  print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
  
elif opc ==2:
  print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))

elif opc == 3:
  print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
  print('Opção inválida')



