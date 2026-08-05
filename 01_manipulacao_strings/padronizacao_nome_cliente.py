nome = str(input('Nome completo do cliente: ')).strip()
print(nome.upper())
print(nome.title())
print('O nome completo do cliente tem: {} letras'.format(len(nome) - nome.count(' ')))
