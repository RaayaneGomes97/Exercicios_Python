print('='*30)
print('10 termos de uma PA')
print('='*30)

p1 = int(input('Primeiro termo: ')) #p1 = primeiro termo
r  = int(input('Razao: ')) # r = razão

termo = p1
cont = 1
p10 = p1 + (10 - 1)*r #Formula de PA para determinar o ultimo termo

print('\n')
while cont <= 10:
  print('{} → '.format(termo), end =' ')
  termo += r 
  cont += 1
print('FIM')
