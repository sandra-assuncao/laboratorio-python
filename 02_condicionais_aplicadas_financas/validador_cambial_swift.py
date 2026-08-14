import random
operacao_dolar = float(input('Digite o valor da operação em dólar: '))
taxa_contratada = float(input('Digite a taxa contratada com o banco: '))
taxa_ptax = round(random.uniform(5.00, 5.40),2)
print('A operação em dólar é no valor de USD {}'.format(operacao_dolar))
print('A taxa PTAX foi {:.4f}'.format(taxa_ptax))
custo_contratado = operacao_dolar * taxa_contratada
print('O custo contratado foi R$ {:.2f}'.format(custo_contratado))
custo_ptax = operacao_dolar * taxa_ptax
print('O custo em PTAX foi R$ {:.2f}'.format(custo_ptax))
variacao_cambial = custo_ptax - custo_contratado
print('A variação cambial foi {:.2f}'.format(variacao_cambial))

if variacao_cambial < 0:
    perda = abs(variacao_cambial)
    print('Análise: Perda Cambial de R$ {:.2f} (Contratado: R$ {:.2f} vs PTAX: R$ {:.2f})'.format(perda, custo_contratado, custo_ptax))
elif variacao_cambial > 0:
    print('Análise: Ganho Cambial / Economia de R$ {:.2f} (Contratado: R$ {:.2f} vs PTAX: R$ {:.2f})'.format(variacao_cambial, custo_contratado, custo_ptax))
else:
    print('Análise: Operação Neutra (Contratado: R$ {:.2f} igual à PTAX: R$ {:.2f})'.format(custo_contratado, custo_ptax))



