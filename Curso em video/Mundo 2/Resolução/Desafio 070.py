
#Inicialização das variaveis
prod1000 = total = menor = cont = 0
barato = '' 

while True:

  produto = str(input('\nNome do produto: '))
  preço   = float(input('Preço R$ '))
  opc = str(input('Deseja continuar? ')).strip().upper()[0]

  cont += 1 #contador
  total += preço

  if preço > 1000:
    prod1000 += 1 #Produtos acima de mil reais

  if cont == 1:
    menor = preço
    barato = produto

  else:
    if preço < menor :
      menor = preço
      barato = produto


 
  # Enerrando o laço
  if opc == 'N':
    break


print('\n' + '-'*30)
print('O total da compra foi R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ R$ 1.000'.format(prod1000))
print('O produto mais barato foi {} custando apenas R$ {:.2f}'.format(barato,menor ))
