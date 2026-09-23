import os
import pandas as pd
import pdfplumber

# --- ETAPA 1: RECONHECER O CONTEÚDO E RENOMEAR OS ARQUIVOS NA PASTA ---

print("=== INICIANDO IDENTIFICAÇÃO E RENOMEAÇÃO DE ARQUIVOS ===")

# Lista todos os arquivos da pasta atual
ficheiros = os.listdir('.')

for f in ficheiros:
    # Ignora scripts python e arquivos consolidados de resultado
    if f.endswith('.py') or f.startswith('Fluxo') or f.startswith('Extrato_Padronizado'):
        continue

    # 1. Verifica se é CSV (Possível Banco do Brasil)
    if f.endswith('.csv'):
        df_temp = pd.read_csv(f, sep=';', header=None, nrows=2)
        conteudo = df_temp.to_string()
        if "BANCO DO BRASIL" in conteudo:
            novo_nome = "Extrato_Padronizado_BB.csv"
            os.rename(f, novo_nome)
            print(f"[RECONHECIDO]: {f} -> Renomeado para {novo_nome}")

    # 2. Verifica se é Excel (.xlsx) (Possível Itaú ou Bradesco)
    elif f.endswith('.xlsx'):
        df_temp = pd.read_excel(f, header=None, nrows=2)
        conteudo = df_temp.to_string()
        if "ITAU" in conteudo:
            novo_nome = "Extrato_Padronizado_Itau.xlsx"
            os.rename(f, novo_nome)
            print(f"[RECONHECIDO]: {f} -> Renomeado para {novo_nome}")
        elif "BRADESCO" in conteudo:
            novo_nome = "Extrato_Padronizado_Bradesco.xlsx"
            os.rename(f, novo_nome)
            print(f"[RECONHECIDO]: {f} -> Renomeado para {novo_nome}")

    # 3. Verifica se é PDF (Possível Santander)
    elif f.endswith('.pdf'):
        # Abre e fecha o PDF para não travar na memória
        with pdfplumber.open(f) as pdf:
            texto_primeira_pagina = pdf.pages[0].extract_text()
        
        # Renomeia fora do bloco 'with' para evitar o PermissionError
        if "SANTANDER" in texto_primeira_pagina:
            novo_nome = "Extrato_Padronizado_Santander.pdf"
            os.rename(f, novo_nome)
            print(f"[RECONHECIDO]: {f} -> Renomeado para {novo_nome}")

print("\n=== RENOMEAÇÃO CONCLUÍDA! INICIANDO TRATAMENTO DE DADOS ===")

# --- ETAPA 2: LER, TRATAR E PADRONIZAR CADA BANCO ---

lista_de_tabelas = []

# 1. TRATAMENTO BANCO DO BRASIL
if os.path.exists("Extrato_Padronizado_BB.csv"):
    df_bb = pd.read_csv("Extrato_Padronizado_BB.csv", sep=';', skiprows=1) # Pula o cabeçalho do banco
    
    # Ajusta o valor com base na coluna Sinal (C/D)
    df_bb['Valor_Limpo'] = df_bb['Valor (R$)'].str.replace(',', '.').astype(float)
    df_bb['Valor Final'] = df_bb.apply(lambda row: -row['Valor_Limpo'] if row['Sinal (C/D)'] == 'D' else row['Valor_Limpo'], axis=1)
    
    # Padroniza as colunas
    df_bb_limpo = pd.DataFrame({
        'Data': df_bb['Data Lançamento'],
        'Banco': 'Banco do Brasil',
        'Descrição': df_bb['Histórico'],
        'Valor (R$)': df_bb['Valor Final']
    })
    lista_de_tabelas.append(df_bb_limpo)

# 2. TRATAMENTO ITAÚ
if os.path.exists("Extrato_Padronizado_Itau.xlsx"):
    df_itau = pd.read_excel("Extrato_Padronizado_Itau.xlsx", skiprows=1)
    
    # Ajusta formato de data do Itaú
    df_itau['Data'] = pd.to_datetime(df_itau['Data']).dt.strftime('%d/%m/%Y')
    
    df_itau_limpo = pd.DataFrame({
        'Data': df_itau['Data'],
        'Banco': 'Itaú Unibanco',
        'Descrição': df_itau['Descrição'],
        'Valor (R$)': df_itau['Valor']
    })
    lista_de_tabelas.append(df_itau_limpo)

# 3. TRATAMENTO BRADESCO
if os.path.exists("Extrato_Padronizado_Bradesco.xlsx"):
    df_bradesco = pd.read_excel("Extrato_Padronizado_Bradesco.xlsx", skiprows=1)
    
    # Unifica Crédito e Débito numa única coluna
    df_bradesco['Valor Final'] = df_bradesco['Crédito (R$)'] - df_bradesco['Débito (R$)']
    
    df_bradesco_limpo = pd.DataFrame({
        'Data': df_bradesco['Data Movimento'],
        'Banco': 'Bradesco',
        'Descrição': df_bradesco['Lançamento'],
        'Valor (R$)': df_bradesco['Valor Final']
    })
    lista_de_tabelas.append(df_bradesco_limpo)

# 4. TRATAMENTO SANTANDER (PDF)
if os.path.exists("Extrato_Padronizado_Santander.pdf"):
    linhas_pdf = []
    with pdfplumber.open("Extrato_Padronizado_Santander.pdf") as pdf:
        tabela = pdf.pages[0].extract_table()
        # Ignora a primeira linha que é o cabeçalho
        for linha in tabela[1:]:
            linhas_pdf.append(linha)
            
    df_santander = pd.DataFrame(linhas_pdf, columns=['Data', 'Descrição', 'Valor'])
    df_santander['Valor (R$)'] = df_santander['Valor'].str.replace(',', '.').astype(float)
    
    df_santander_limpo = pd.DataFrame({
        'Data': df_santander['Data'],
        'Banco': 'Santander',
        'Descrição': df_santander['Descrição'],
        'Valor (R$)': df_santander['Valor (R$)']
    })
    lista_de_tabelas.append(df_santander_limpo)

# --- ETAPA 3: CONSOLIDAÇÃO E SALVAMENTO ---

if lista_de_tabelas:
    extrato_consolidado = pd.concat(lista_de_tabelas, ignore_index=True)
    extrato_consolidado.to_excel("Fluxo_de_Caixa_Consolidado_MultiBancos.xlsx", index=False)
    print("\n>>> SUCESSO! Todos os extratos foram renomeados, tratados e consolidados na planilha final! <<<")
else:
    print("\n[AVISO] Nenhuma tabela foi encontrada para consolidar. Certifique-se de ter rodado o 'gerar_arquivos_ficticios.py' primeiro.")