# 🏛️ Automação e Consolidação Inteligente de Extratos Multibancos

Este projeto resolve um problema crítico e recorrente nas rotinas de **Tesouraria e Controladoria**: a reconciliação e consolidação de extratos bancários de múltiplos bancos (Banco do Brasil, Itaú, Bradesco e Santander), recebidos em diferentes formatos (CSV, Excel e PDF) e com nomenclatura de arquivos não padronizada.

A solução substitui o trabalho manual e suscetível a erros de "copiar e colar" por um **script robusto em Python**, desenvolvido no **Visual Studio Code (VS Code)**, capaz de reconhecer o conteúdo do arquivo, padronizar a nomenclatura no disco, tratar os dados específicos de cada instituição e unificar o fluxo de caixa em menos de 1 segundo.

---

## 🎯 Problema de Negócio

No dia a dia corporativo, a equipe financeira precisa baixar extratos bancários de diferentes plataformas. Esse processo gera:

* **Heterogeneidade de Formatos:** Cada banco exporta dados em layouts próprios (colunas separadas de débito/crédito, sinais `C` / `D`, datas em formatos mistos).
* **Nomes Aleatórios:** Downloads gerados com nomes genéricos ou temporários (ex: `download_temp_98213.csv`, `extrato_scanned.pdf`).
* **Incompatibilidade de PDFs:** Arquivos em PDF que exigem extração via OCR/leitura estruturada antes da manipulação.
* **Gargalo Operacional:** Média de **30 a 45 minutos diários** gastando apenas em formatação e unificação manual de planilhas.

---

## 🚀 Solução Desenvolvida

O script `consolidador_inteligente.py` atua em **3 etapas automatizadas**:

1. **Reconhecimento de Conteúdo & Renomeação Automática:**
   * Leitura rápida dos metadados e primeiras linhas dos arquivos na pasta sem carregar volumes desnecessários na memória.
   * Identificação do banco emissor por "pegadas digitais" do conteúdo interno.
   * Renomeação padronizada no sistema operacional (`os.rename`).

2. **Tratamento e Normalização de Dados:**
   * **Banco do Brasil (CSV):** Conversão de decimais, aplicação de regra de sinal (`C` / `D` para positivo/negativo) via `apply` e `lambda`.
   * **Itaú (XLSX):** Padronização do formato de data (`DD/MM/YYYY`).
   * **Bradesco (XLSX):** Unificação de colunas isoladas de Crédito e Débito numa única coluna de valor líquido.
   * **Santander (PDF):** Extração tabular via `pdfplumber` com fechamento seguro de memória para prevenção de erros do sistema.

3. **Consolidação Final & Exportação:**
   * Empilhamento dos DataFrames limpos usando `pd.concat`.
   * Exportação para uma planilha unificada `Fluxo_de_Caixa_Consolidado_MultiBancos.xlsx`.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **VS Code (Visual Studio Code):** Ambiente de desenvolvimento integrado (IDE) utilizado na escrita, depuração e execução dos scripts Python.
* **Python 3.x:** Linguagem base da automação.
* **Pandas:** Leitura, limpeza, transformação e consolidação tabular de dados (CSV e XLSX).
* **pdfplumber:** Leitura, parsing e extração de tabelas de arquivos PDF.
* **OS (Nativo):** Manipulação direta de arquivos do sistema operacional.
* **FPDF:** Utilizado na construção da massa de testes fictícia simulando dados bancários reais.

---

## 📈 Resultados e Impactos

* **Redução Drástica de Tempo:** O tempo de execução da rotina foi reduzido de **~40 minutos diários manuais** para um processamento em **sub-segundo (menos de 1 segundo)**.
* **Integridade e Confiabilidade dos Dados:** Mitigação total de falhas humanas na cópia, digitação ou formatação manual de valores financeiros.
* **Escalabilidade:** Estrutura modular preparada para receber novos bancos, formatos ou volumes maiores de transações sem necessidade de reescrever a arquitetura.

---

## 📂 Estrutura dos Arquivos

├── consolidador_inteligente.py   # Script principal de automação e consolidação
├── gerar_arquivos_ficticios.py   # Script utilitário para geração de massa de dados
├── Extrato_Padronizado_BB.csv     # Extrato tratado (Banco do Brasil)
├── Extrato_Padronizado_Itau.xlsx # Extrato tratado (Itaú)
├── Extrato_Padronizado_Bradesco.xlsx # Extrato tratado (Bradesco)
├── Extrato_Padronizado_Santander.pdf # Extrato tratado (Santander)
└── Fluxo_de_Caixa_Consolidado_MultiBancos.xlsx # Resultado final consolidado
