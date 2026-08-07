# Solução para Padronização e Análise de Nome do Cliente

nome = str(input('Nome completo do cliente: ')).strip()

print('\n--- Resultados ---')
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome formatado: {nome.title()}')

# Abordagem 1: Lógica Matemática (Tamanho total - quantidade de espaços)
letras_matematica = len(nome) - nome.count(' ')
print(f'Total de letras (via cálculo matemático): {letras_matematica}')

# Abordagem 2: Manipulação de Texto (Separa em lista e junta sem espaços)
letras_string = len(''.join(nome.split()))
print(f'Total de letras (via manipulação de strings): {letras_string}')
