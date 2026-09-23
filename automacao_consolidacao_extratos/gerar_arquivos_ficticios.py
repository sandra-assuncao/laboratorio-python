import pandas as pd
from fpdf import FPDF

# 1. BANCO DO BRASIL (CSV com nome genérico e linha de cabeçalho do banco)
dados_bb = [
    ["BANCO DO BRASIL S.A.", "", "", "", ""], # Linha 1 identificadora do banco
    ["Data Lançamento", "Histórico", "Valor (R$)", "Sinal (C/D)", "Saldo"],
    ["01/09/2026", "Pagto Fornecedor A", "1500,00", "D", "10500,00"],
    ["01/09/2026", "Recebimento Cliente X", "5000,00", "C", "15500,00"],
    ["02/09/2026", "Tarifa Bancaria", "45,00", "D", "15455,00"]
]
df_bb = pd.DataFrame(dados_bb)
# Salva com nome aleatório de download
df_bb.to_csv("download_temp_98213.csv", sep=";", index=False, header=False, encoding="utf-8-sig")

# 2. ITAÚ (Excel com nome genérico e cabeçalho identificador)
dados_itau = [
    ["BANCO ITAU UNIBANCO S.A.", "", "", ""], # Linha 1 identificadora
    ["Data", "Descrição", "Valor", "Tipo"],
    ["2026-09-01", "Pagamento Fornecedor A", -2352.00, "Saida"],
    ["2026-09-01", "Recebimento Cliente X", 12356.00, "Entrada"],
    ["2026-09-02", "Tarifa Bancaria", -206.00, "Saida"]
]
df_itau = pd.DataFrame(dados_itau)
# Salva com nome aleatório de download
df_itau.to_excel("export_ext_2026.xlsx", index=False, header=False)

# 3. BRADESCO (Excel com nome genérico e cabeçalho identificador)
dados_bradesco = [
    ["BANCO BRADESCO S.A.", "", "", "", ""], # Linha 1 identificadora
    ["Data Movimento", "Lançamento", "Documento", "Crédito (R$)", "Débito (R$)"],
    ["01/09/2026", "Pagamento Fornecedor A", "DOC101", 0.00, 13568.00],
    ["01/09/2026", "Recebimento Cliente X", "DOC102", 6753.00, 0.00],
    ["02/09/2026", "Tarifa Bancaria", "DOC103", 0.00, 523.00]
]
df_bradesco = pd.DataFrame(dados_bradesco)
# Salva com nome aleatório de download
df_bradesco.to_excel("relatorio_mov_01.xlsx", index=False, header=False)

# 4. SANTANDER (PDF com layout impresso e nome genérico)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, text="BANCO SANTANDER - EXTRATO DE CONTA CORRENTE", new_x="LMARGIN", new_y="NEXT", align='C')
pdf.ln(10)

pdf.set_font("Arial", 'B', 10)
pdf.cell(30, 8, "Data", border=1)
pdf.cell(110, 8, "Historico da Operacao", border=1)
pdf.cell(40, 8, "Valor R$", border=1)
pdf.ln()

pdf.set_font("Arial", '', 10)
dados_pdf = [
    ("01/09/2026", "Pagamento Fornecedor A", "-4120,50"),
    ("01/09/2026", "Recebimento Cliente X", "8900,00"),
    ("02/09/2026", "Tarifa Mensal Conta", "-89,90")
]

for data, hist, val in dados_pdf:
    pdf.cell(30, 8, data, border=1)
    pdf.cell(110, 8, hist, border=1)
    pdf.cell(40, 8, val, border=1)
    pdf.ln()

# Salva com nome aleatório de download
pdf.output("extrato_scanned.pdf")

print(">>> Novos arquivos de teste com nomes genéricos e identificadores internos foram gerados! <<<")