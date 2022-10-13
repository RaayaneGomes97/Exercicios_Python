# Exercicio 33

A  = int(input('Informe um valor para A: '))
B  = int(input('Informe um valor para B: '))
C  = int(input('Informe um valor para C: '))

print('-'*30)
if A > B > C:
  print('O menor valor digitado foi {}'.format(A))
  print('O maior valor digitado foi {}'.format(C))
if A > C > B:
  print('O menor valor digitado foi {}'.format(B))
  print('O maior valor digitado foi {}'.format(A))


if B > C > A:
  print('O menor valor digitado foi {}'.format(A))
  print('O maior valor digitado foi {}'.format(B))
if B > A > C:
  print('O menor valor digitado foi {}'.format(C))
  print('O maior valor digitado foi {}'.format(B))


if C > A > B:
  print('O menor valor digitado foi {}'.format(B))
  print('O maior valor digitado foi {}'.format(C))
if C > B > A:
  print('O menor valor digitado foi {}'.format(A))
  print('O maior valor digitado foi {}'.format(C))
