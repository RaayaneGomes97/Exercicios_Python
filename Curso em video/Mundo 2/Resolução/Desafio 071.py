
from math import trunc #Importação necessária para execut funcionalidade Trunc




#Inicialização das variaveis responsáveis a armazenar quantas cédulas serão necessárias
ced5 = ced10 = ced20 = ced50 = 0
print('━'*50) #Organização
print('┃         SIMULADOR DE CAIXA ELETRÔNICO          ┃')




while True:  #Looping infinito, Só será interrompido com uso do Break. 
# (Não tenho propósito de interrompe-lo nesse algoritmo)
  print('━'*50) 

 #Entrada dados de numeros inteiros, apenas.
  saldo = float(input('\nQuanto você quer retirar? R$ '))

  print('\n') #Quebra de linha



  #cALCULANDO CÉDULAS DE 50 -----------------------------

  if saldo > 50 : #APENAS SE o saldo for maior que 50 ele executa
    ced50 = (trunc(saldo/50)) # Dividindo por 50 e pegando parte inteira do resultado
    saldo -= (ced50)*50 #Atualizando o saldo subtraindo do troco que já foi dado
    print('Total de {} cédulas de R$ 50'.format(ced50))





  #cALCULANDO CÉDULAS DE 20 -----------------------------
  if saldo  >= 20:
    ced20 = (trunc(saldo/20)) # Dividindo por 20 e pegando parte inteira do resultado
    saldo -= (ced20)*20 #Atualizando o saldo subtraindo do troco que já foi dado
    print('Total de {} cédulas de R$ 20'.format(ced20))





  #cALCULANDO CÉDULAS DE 10 -----------------------------
  if saldo  >= 10:
    ced10 = (trunc(saldo/10)) # Dividindo por 10 e pegando parte inteira do resultado
    saldo -= (ced10)*10 #Atualizando o saldo subtraindo do troco que já foi dado
    print('Total de {} cédulas de R$ 10'.format(ced10))






  #cALCULANDO CÉDULAS DE 1 -----------------------------

  if saldo >= 1:
    ced1 = (trunc(saldo/1)) # Dividindo por 1 e pegando parte inteira do resultado
    saldo -= (ced1)*1 #Atualizando o saldo
    print('Total de {} cédulas de R$ 1'.format(ced1))
