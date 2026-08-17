## 1. Validador de Repasse de Adquirente & Taxa MDR (Contas a Receber)
## A regra de negócio: O sistema lê o valor bruto de uma venda no cartão e a taxa MDR contratada (ex: 2.5%). O usuário digita o valor líquido que caiu no extrato bancário.
## O if/else: O Python calcula qual deveria ser o repasse correto e verifica se o valor que caiu na conta bate com o esperado ou se houve divergência/cobrança indevida de taxa.


valor_bruto = float(input('Digite o valor bruto da venda R$: '))
print('O valor bruto da venda foi R$ {}'.format(valor_bruto))

valor_liquido = float(input('Digite o valor líquido da venda recebido no extrato bancário R$: '))
print('O valor líquido da venda recebido no extrato bancário foi R$ {:.2f}'.format(valor_liquido))

taxa_mdr = 0.025 # 2.5%
valor_liquido_esperado = valor_bruto * (1- taxa_mdr)

diferenca = abs(valor_liquido_esperado - valor_liquido)
taxa_efetiva =((valor_bruto - valor_liquido) / valor_bruto) * 100

print('-' * 40)

if valor_liquido == valor_liquido_esperado:
    print('A taxa MDR foi cobrada corretamente (2.5%).')
elif valor_liquido < valor_liquido_esperado:
    print('Atenção: Cobrança INDEVIDA A MAIOR pela adquirente!')
    print('Foi cobrado R$ {:.2f} A MAIS do que o esperado.'.format(diferenca))
    print('A taxa MDR aplicado no extrato foi de {:.2f}% (Contratado: 2.5%).'.format(taxa_efetiva))
else:
    print('Atenção: Valor recebido A MAIOR do que esperado!')
    print('Entrou R$ {:.2f} a mais no caixa.'.format(diferenca))
    print('A taxa MDR aplicada no extrato foi de {:.2f}% (Contratado: 2.5%).'.format(taxa_efetiva))

