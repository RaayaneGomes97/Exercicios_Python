
print('='*30)
print('10 termos de uma PA')
print('='*30)

p1    = int(input('Primeiro termo: '))
r = int(input('Razao: '))

p10 = p1 + (10 - 1)*r #Formula de PA para determinar o ultimo termo

print('\n')

for x in range(p1, p10 + r, r):
  print('{}'.format(x), end=  ' → ' )
