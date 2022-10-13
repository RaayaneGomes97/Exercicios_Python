

<table class="gn-seletable">
<tbody><tr>
<th><a href="https://github.com/RayaneGomes97/Exercicios_Python/blob/master/README.md"> Voltar ao menu incial</a></th>
<th>Acessar  lista</th>
<th><a href="https://github.com/RayaneGomes97/Exercicios_Python/blob/master/Kaggle%20Notebooks/Introdu%C3%A7%C3%A3o%20a%20analise%20de%20dados/status.md">Verificar status </a></th>
  <th><a href="https://github.com/RayaneGomes97/Exercicios_Python/tree/master/Exercicios%20com%20String_PythonOrg/Resolu%C3%A7%C3%A3o">Consultar respostas</a></th></table>


<!-- -------------------------------------------------------- -->


<h3><a href="#home"> 💻</a> Seleções Básicas </h3>	
<br> <strong> 1. </strong> Selecionar as 10 primeiras linhas mostrando as colunas municipio, estado e idhm.
<br> <strong> 2. </strong> Selecionar das linhas 15 a 24 os valores da coluna municipio
  
----

 <h3><a href="#home"> 💻</a> Series </h3>	
<br> <strong> 3. </strong> Contar o número de munícipios por estado.
<br> <strong> 4. </strong> Plotar gráfico de número de munícipios por estado
 
----
 <h3><a href="#home"> 💻</a> Agregações Númericas </h3>	
<br> <strong> 5. </strong> Utilize o .min(), .max(), e .mean() para avaliar os dados da coluna exp_vida
<br> <strong> 6. </strong> Plotar gráfico de número de munícipios por estadoUtilize o .describe() para avaliar os dados da coluna idhm
    
----
 <h3><a href="#home"> 💻</a> Histogramas </h3>	
<br> <strong> 7. </strong> Plote um histograma do gasto_pc_educacao
<br> <strong> 8. </strong> Plote um sns.kdeplot() do gasto_pc_educacao
<br> <strong> 9. </strong> Plote um sns.distplot() do gasto_pc_educacao
<br> <strong> 10. </strong> Utilize o .describe() para ver os valores numéricos do gasto_pc_educacao
  
----
 <h3><a href="#home"> 💻</a> Mais filtros e Shape </h3>	
<br> <strong> 11. </strong> Crie um filtro chamado meu_filtro para selecionar apenas as linhas onde os valores da coluna pib_pc sejam maiores do que 50000
<br> <strong> 12. </strong> Crie um novo DataFrame chamado igm_filtrado_pib_pc aplicando o meu_filtro no igm
<br> <strong> 13. </strong> Utilize o método .describe() na coluna pib_pc do igm_filtrado_pib_pc
<br> <strong> 14. </strong> Plote um histograma da coluna pib_pc do igm_filtrado_pib_pc

----

 <h3><a href="#strings"> 💻</a> Manipulação de Strings </h3>	
<br> <strong> 15. </strong> Transforme a coluna ranking_igm para uma coluna numéricA
<br> <strong> 16. </strong>Crie uma coluna comissionados_por_servidor_2 a partir das colunas comissionados e servidores
<br> <strong> 17. </strong> Substitua a coluna comissionados_por_servidor se for o caso
<br> <strong> 18. </strong> Delete a coluna comissionados_por_servidor_2

----

 <h3><a href="#home"> 💻</a> Revisão </h3>	

<br> <strong> 19. </strong> Plotar um histograma da coluna exp_vida
<br> <strong> 20. </strong> Usar o método .describe na coluna exp_vida
<br> <strong> 21. </strong> Usar o método .describe na coluna exp_vida onde os municípios sejam apenas da região NORTE
<br> <strong> 22. </strong> Usar o método .value_counts() na coluna estado filtrando os munícipios que tenham pib_pc > 50000
<br> <strong> 23. </strong> Usar o método .value_counts() na coluna estado filtrando os munícipios que tenham pib_pc > 50000
<br> <strong> 24. </strong> Plotar um gráfico de barras do resultado gerado pelo item 4


----

<h3><a href="#home"> 💻</a> Histogramas Interativos </h3>	

<br> <strong> 25 </strong> Plote um histograma interativo de 2 colunas da sua escolha.


----

 <h3><a href="#home"> 💻</a> Importando arquivos </h3>	

<br> <strong> 26. </strong> Importe o arquivo dados_inpe.xlsx usando a função pd.read_excel().
<br> <strong> 27. </strong> Importe novamente o arquivo ajustando os parâmetros header e skip_footer
<br> <strong> 28. </strong> Averigue o DataFrame gerado no item 2. Use o comando .info().
<br> <strong> 29. </strong> Importe o arquivo anexo-V.csv, usando o read_csv() e o parâmetro encoding='latin1'. (Ignore o DTypeWarning caso aconteça, ou use o parâmetro low_memory=False)
<br> <strong> 30. </strong> Importe novamente o arquivo ajustando o parâmetro header e salve o DataFrame em uma variável com o nome de anexo.
<br> <strong> 31. </strong> Averigue a variável anexo com o comando .info().

----

 <h3><a href="#home"> 💻</a> Plotando Múltiplos Gráficos </h3>	

<br> <strong> 32. </strong> Plote os gráficos de exp_vidade acordo com o porte
<br> <strong> 33. </strong> Adicione legendas ao gráfico

----

 <h3><a href="#vis"> 💻</a> Visualizando Categorias </h3>	

<br> <strong> 34. </strong> Fazer um boxplot de porte no eixo x e exp_vida no eixo y
<br> <strong> 35. </strong> Fazer um violinplot de porte no eixo x e exp_vida no eixo y com hue=regiao
<br> <strong> 36. </strong> Criar um factorplot do tipo box com porte no eixo x e exp_vida no eixo y e col='regiao'
<br> <strong> 37. </strong> Pegar o factorplot do item 1 e substituir col='regiao' por row='regiao'
<br> <strong> 38. </strong> Fazer um factorplot usando kind='count', hue='porte' e x='regiao'
<br> <strong> 39. </strong> Criar uma coluna sem_gasto_pc_saude a partir dos valores em branco da coluna gasto_pc_saude
<br> <strong> 40. </strong> Criar uma coluna cat_te separando os valores em 3 categorias pra qcut
<br> <strong> 41. </strong> Criar um factorplot do tipo box com porte no eixo x e exp_vida no eixo y e col='regiao' e row='cat_te
<br> <strong> 42. </strong> Facilite a leitura dos nomes das regiões. Dica: g.set_xticklabels(rotation=30)



----

 <h3><a href="#home"> 💻</a> Mais gráficos categóricos </h3>	

<br> <strong> 43. </strong> Fazer um gráfico a partir do agrupamento de porte avaliando gasto_pc_saude
<br> <strong> 44. </strong> Fazer o exercício 1 a partir de um groupby()
<br> <strong> 45. </strong> Fazer um swarmplot usando y="gasto_pc_saude", hue='porte'

----

 <h3><a href="#home"> 💻</a> Explorando Variáveis Contínuas </h3>	

<br> <strong> 46. </strong> Fazer um pairplot usando taxa_empreendedorismo e nota_mat usando hue=porte (apenas 1 gráfico e não 4)
<br> <strong> 47. </strong> Fazer um pairplot usando taxa_empreendedorismo e nota_mat usando hue=porte (4 gráficos)
<br> <strong> 48. </strong> Fazer um pairplot usando taxa_empreendedorismo, anos_estudo_empreendedor, nota_mat e idhm, usando hue=porte

----
 <h3><a href="#home"> 💻</a> Plots usando Escala logarítimica </h3>	

<br> <strong> 49. </strong> Plote um pairplot de anos_estudo_empreendedor por pib_pc
  <br> <strong> 50. </strong> Crie uma nova variável chamada log_pib_pc com o log de pib_pc
<br> <strong> 51. </strong> Plote um pairplot de anos_estudo_empreendedor por log_pib_pc
