times = (
  'Flamengo', 'Santos','Palmeiras','Grêmio','Athlético-PR',
  'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
  'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
  'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense','Avaí')

# 5 primeiros colocados: OK
# 4 ultimos 4 colocados na tabela : X
# Uma lista em ordem alfabética: OK
# Em que posição está chapecoense: OK

print(f'\n\n  Lista do brasileirão: { times }')

print(f'\n\n1) Os 5 primeiros são { times[0:5] }')

print(f'\n\n2) Os 4 ultimos são { times[-4:] }') #Ordem trás pra frente: -1 -2 -3 -4...

print(f'\n\n3) Times em ordem alfabética: { sorted(times) }')
#Sorted não altera a ordem da tupla, ele apenas ordena ela.

print(f'\n\n4) Posição do Chapecoense: {  times.index("Chapecoense")+1  }°')
#Index retorna a posição de um elemento

