# Análise Exploratória de Dados

## O Hospital das Clínicas de Pernambuco - Consultas especialistas no 2º semestre de 2022.

[Base de Dados (Disponibilizada no Open Data do Governo)](https://github.com/Tomasi/AnaliseExploratoriaDados/blob/7199759e7bf66217464e687db0cefac710949c7a/consultas_realizadas_por_especialidade_hc_ufpe_jul_a_dez22-fevereiro-2023.xlsx)

# Introdução

Esta análise exploratório compreende a importância de especialidades em diversas areas da saúde e afim de traçar um perfil de maior procura em consultas com especilistas, utilizando como base o período do 2º semestre de 2022. O open data disponibilizado pelo [Hospital das Clínicas de Pernambuco](https://www.gov.br/ebserh/pt-br/hospitais-universitarios/regiao-nordeste/hc-ufpe) será usado como ferramenta.

# Materiais e Métodos

Os dados são compostos pelo setor de especialidade, quantidade de consultas apontadas no mês e o total de consultas realizadas no fechamento do período.

1. GoogleColab

O Google Colab é um ambiente de desenvolvimento integrado (IDE) baseado na nuvem que permite a criação e execução de notebooks Jupyter usando o recurso de computação em nuvem do Google. Com o Google Colab, os usuários podem escrever e executar código Python diretamente no navegador, também possui recursos integrados para visualização de dados.

2. Colunas/Tipo

Ambulatório (Especialidade) = Categórico

jul/2022 = Quantitativo

ago/2022 = Quantitativo

set/2022 = Quantitativo

out/2022 = Quantitativo

nov/2022 = Quantitativo

dez/2022 = Quantitativo

total    = Quantitativo

# Extração e Limpeza de Dados

Durante a analise exploratório, senti necessidade de limpar e formatar o dataset. Os tipos das colunas encontravam-se como 'object', comecei formatando os dados para seus tipos corretos. Com o objetivo de não "interferir" nos resultados, removi também a última linha do dataSet, que referia-se à sumarização das colunas.

# Histograma

![histograma.png](https://github.com/Tomasi/AnaliseExploratoriaDados/blob/master/histograma.png)

# CDFs

![ecdf.png](https://github.com/Tomasi/AnaliseExploratoriaDados/blob/master/ecdf.png)

# Tendências Centrais

a.Mínimo : 5

b.Máximo : 9468

c.Média :  2345.612245

d.Mediana : 1882

e.Moda : 832

f.Desvio padrão : 2126.9891224914622

g.Variância : 4618334.450680272

