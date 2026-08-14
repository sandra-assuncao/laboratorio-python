# 💱 Validador de Variação Cambial (Operações SWIFT)

Este script foi desenvolvido para simular e validar o impacto financeiro de liquidações em moeda estrangeira (USD) em relação à taxa PTAX oficial do dia, automatizando a identificação de perdas ou ganhos cambiais.

---

## 🎯 Objetivo de Negócio
Em operações de comércio exterior e tesouraria internacional, a divergência entre a taxa de câmbio contratada com a instituição financeira e a PTAX do dia gera variações que impactam o resultado do caixa. O objetivo deste projeto é entregar uma **análise executiva automática** informando se a operação gerou:
* **Perda Cambial:** Custo contratado acima da PTAX.
* **Ganho Cambial / Economia:** Custo contratado abaixo da PTAX.
* **Operação Neutra:** Taxas equivalentes.

---

## 💻 Conceitos Técnicos Aplicados (Python)
* **Estruturas Condicionais (`if` / `elif` / `else`):** Mapeamento e tratamento de cenários financeiros distintos.
* **Tratamento de Números Negativos (`abs()`):** Para exibição clara do valor monetário da perda sem sinal negativo redundante.
* **Simulação de Dados (`random.uniform`):** Geração dinâmica da taxa PTAX do dia para testes de estresse.
* **Formatação de Saída (`.format()` / `{:.2f}`):** Padronização de valores decimais e moeda (R$).

---

## 📊 Exemplo de Saída no Terminal
```text
Digite o valor da operação em dólar: 15234.98
Digite a taxa contratada com o banco: 5.4567

A operação em dólar é no valor de USD 15234.98
A taxa PTAX foi 5.3900
O custo contratado foi R$ 83132.72
O custo em PTAX foi R$ 82116.54
A variação cambial foi -1016.17

Análise: Perda Cambial de R$ 1016.17 (Contratado: R$ 83132.72 vs PTAX: R$ 82116.54)
