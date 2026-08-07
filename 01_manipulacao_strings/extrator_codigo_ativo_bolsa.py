# ENTRADA E PADRONIZAÇÃO DOS DADOS
codigo_ativo = str(input('Código do ativo e descrição da bolsa de valores B3: ')).strip().upper()

# SEPARAÇÃO DO TICKER
codigo_separado = codigo_ativo.split()
ticker = codigo_separado[0]

# VERIFICAÇÃO SE É AÇÃO PREFERENCIAL (PN)
acao_preferencial = '4' in ticker

# EXIBIÇÃO DOS RESULTADOS
print(f'Ticker extraído: {ticker}')
print(f'É uma ação Preferencial (PN)? {acao_preferencial}')

