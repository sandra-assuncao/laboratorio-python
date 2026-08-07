# ENTRADA DE DADOS
chave_pix = str(input('Digite a chave PIX (CPF): ')).strip()
numero_cartao = str(input('Digite o número do cartão: ')).strip()

# TRATAMENTO E REMOÇÃO DE CARACTERES ESPECIAIS
chave_pix = chave_pix.replace('.', '').replace('-', '').replace(' ', '')
numero_cartao = numero_cartao.replace('.', '').replace('-', '').replace(' ', '')

# EXTRAÇÃO DE DIGITOS E MONTAGEM DAS MÁSCARAS
primeiros_3 = chave_pix[:3]
ultimos_2 = chave_pix[-2:]
mascara_cpf = '{}.***.***-{}'.format(primeiros_3, ultimos_2)

primeiros_4 = numero_cartao[:4]
ultimos_4 = numero_cartao[-4:]
mascara_cartao = '{}.****.****-{}'.format(primeiros_4, ultimos_4)

# EXIBIÇÃO DOS RESULTADOS
print(f'A chave PIX tem {len(chave_pix)} dígitos.')
print(f'O número do cartão tem {len(numero_cartao)} dígitos.')
print(f'CPF mascarado: {mascara_cpf}')
print(f'Cartão mascarado: {mascara_cartao}')
