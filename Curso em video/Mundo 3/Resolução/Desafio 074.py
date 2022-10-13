from random import randint
x = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print('Os valores sorteados foram {}'.format(x)) 

print(f'\nO maior sorteado foi {max(x)}')
print(f'O menor sorteado foi {min(x)}')
