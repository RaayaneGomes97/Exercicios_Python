#Desafio 39

print('Estaremos tomando como base o ano que o exercício foi realizado')

print('-'*50) # -----

nasc = int(input('Ano de nascimento: ')) #nasc = nascimento

ano = 2017
idade = ano - nasc
alist = (18 - idade)
data = alist + ano

print('Quem nasceu em {} tem {} anos\n em  {}'.format(nasc,idade,ano))

if idade == 18:
  print('Você precisa se alistar IMEDIATAMENTE')

if idade < 18:
  print('''
  Ainda faltam {} anos para seu alistamento militar.
  Seu alistamento militar será em {}
  '''''.format(alist, data))


elif idade > 18: 
  print(''' 
  Você já deveria ter se alistado há {} anos.
  Seu alistamento foi em {}
  '''''.format(alist*-1, data))

# ------------ Solução proposta pelo curso: ------------

# Poderia ter importado a biblioteca datetime e usado a função date para pegar o ano atual. Dessa forma:

# from datetime import date
# ano = date.today().year 

# Nesse caso estariamos pegando o ano atual e armazenando na variavel "ano".

# Maiores informações sobre módulos na aula 08: Mundo 1 - Python[Curso em vídeo]
