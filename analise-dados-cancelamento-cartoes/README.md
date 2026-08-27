# 📊 Análise de Cancelamento de Clientes (Churn - Cartões de Crédito)

## 🎯 Objetivo do Projeto
Identificar os principais motivos pelos quais os clientes de um banco estão cancelando seus cartões de crédito e propor soluções estratégicas para a diretoria conter a perda de receita.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
- **Linguagem:** Python
- **Ambiente:** Google Colab
- **Manipulação e Tratamento de Dados:** Pandas
- **Visualização de Dados:** Plotly Express

---

## 📋 Etapas do Projeto
1. **Importação dos Dados:** Conexão com o Google Drive e carregamento do dataset.
2. **Tratamento da Base:** Remoção de colunas irrelevantes (`CLIENTNUM`) e eliminação de valores vazios com `dropna()`.
3. **Análise Exploratória:** Verificação das métricas estatísticas e distribuição das categorias (Clientes Ativos vs. Cancelados).
4. **Análise de Hipóteses com Laço `for`:** Criação automatizada de histogramas interativos comparando cada coluna do dataset com a variável principal (`Categoria`).

---

## 💡 Principais Insights da Análise
A partir da visualização dos gráficos gerados, foram identificados três padrões comportamentais claros nos clientes que cancelam o cartão:

* **Quantidade de Produtos:** Quanto menos produtos contratados o cliente possui, maior a chance de cancelamento.
* **Volume de Uso e Transações:** Clientes com menor número e menor valor total de transações apresentam taxa de *churn* elevadíssima.
* **Contatos com o Suporte:** Quanto maior a quantidade de contatos que o cliente precisou fazer com a empresa, maior a probabilidade dele cancelar o serviço.

---

## 🚀 Recomendações Estratégicas para o Negócio
- **Campanhas de Engajamento:** Criar incentivos e vantagens para estimular o uso do cartão em pequenas transações do dia a dia.
- **Cross-selling:** Promover a adesão a novos produtos/serviços para clientes que possuem apenas 1 ou 2 produtos contratados.
- **Alerta no Atendimento:** Priorizar e monitorar atendimentos de clientes que já entraram em contato mais de 2 vezes com o suporte para evitar insatisfações e retenção preventiva.
