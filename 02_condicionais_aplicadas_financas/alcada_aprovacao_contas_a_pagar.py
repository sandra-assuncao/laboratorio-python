## A regra de negócio: O usuário informa o valor total de um lote de pagamentos (TED/Tributos/Fornecedores)
## O if/else: O script verifica os limites da empresa:
## Até R$ 50.000 → Aprovação automática pelo Analista;
## Acima de R$ 50.000 → Requer dupla aprovação do Gerente de Tesouraria;
## Acima do limite da conta bancária → Alerta de Saldo Insuficiente / Risco de Descoberto.


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
