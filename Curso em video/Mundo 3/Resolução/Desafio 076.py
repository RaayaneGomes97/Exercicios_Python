listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.50,
            'Estojo', 25,
            'Transferidor', 4.50,
            'Compasso', 9.99,
            'Mochila', 120.50)
            
    # Perceba que numero do produto segue numa posição par
    # E o valor dele numa posição impar, logo:

for x in range(0,len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<30}', end=' ') # Alinha a esquerda
    else:
        print(f'R${listagem[x]:>7.2f}')
