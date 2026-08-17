nome_fornecedor = str(input('Digite o nome do fornecedor: '))
print('Fornecedor: {}'.format(nome_fornecedor))
valor_a_pagar = float(input('Digite o valor do pagamento do título R$: '))
print('O valor a ser pago é R$ {:.2f}'.format(valor_a_pagar))

print('-' * 40)

if valor_a_pagar <= 5000.00:
    print('Aprovação automática pelo Analista de Contas a Pagar')
elif valor_a_pagar <= 50000.00:
    print('Requer aprovação do Gerente Financeiro.')
else:
    print('Requer aprovação da Diretoria / CFO.')
