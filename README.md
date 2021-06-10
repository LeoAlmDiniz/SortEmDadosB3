Neste case, mostro como acessar uma tabela em formato HTML na página da B3 e transformá-la em uma planilha Excel e organizar os dados de acordo com sua participação
no índice Bovespa em ordem decrescente, utilizando o Pandas. Logo após, mostro como baixar a tabela em formato CSV da mesma página, organizar os dados utilizando o Pandas e salvar este arquivo CSV.

Instruções (necessário ter versão 3 do Python instalada)
1. No terminal, instalar os pacotes requeridos: pip install -m requirements.txt;
2. No terminal, rodar case1.py: o código irá baixar a tabela disponível em no link http://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm e transformará ela em um arquivo chamado case1_output em formato xslx para Excel.
3. No terminal, rodar case2.py: o código irá acessar a planilha IBOVDia_10-06-21.csv, organizá-la em ordem decrescente de participação e salvar em um novo arquivo case2_output.csv compatível com Excel.