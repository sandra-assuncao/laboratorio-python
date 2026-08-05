nome = str(input('Nome completo do cliente: ')).strip()
print(nome.upper())
print(nome.title())
print('O nome completo do cliente tem: {}'.format(len(''.join(nome.split()))))
