# 🐍 Laboratório de Python para Finanças & Dados

Este repositório reúne scripts, desafios e pequenos projetos focados na automação de processos, sanitização de dados e resolução de problemas práticos do mercado financeiro e de tesouraria.

---

## 📌 Conteúdo do Repositório

### 1. Sanitização e Padronização de Cadastros (`01_manipulacao_strings`)
Desafio focado no tratamento de dados de entrada de clientes para geração de contratos, e-mails e relatórios financeiros sem erros.

* **`padronizacao_nome_cliente.py`**:
  * **Abordagem:** Matemática (`len()` e `.count()`).
  * **Objetivo:** Formatação em maiúsculas, formato de título e cálculo exato da quantidade de letras descartando espaços internos.
* **`padronizacao_nome_cliente_v2.py`**:
  * **Abordagem:** Manipulação de listas e textos (`.split()` e `.join()`).
  * **Objetivo:** Mesma regra de negócio da versão 1, explorando uma lógica alternativa para remoção de espaços e contagem de caracteres.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Conceitos de Strings:** `.strip()`, `.upper()`, `.title()`, `.split()`, `.join()`
* **Lógica e Métricas:** `len()`, `.count()`
* **Interatividade:** `input()`, interpolação com `.format()` e *f-strings*

---

## 🚀 Como Executar os Scripts

1. Clone este repositório:
```bash
git clone https://github.com/sandra-assuncao/laboratorio-python.git
