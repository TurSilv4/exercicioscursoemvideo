print('{:-^32}'.format(''' Arthur's Store '''))
print('')

produto = float(input('Qual o valor a ser pago: R$'))
print('FORMA DE PAGAMENTO: ')
forma_pagamento = int(input(' [1] A vista\n'
                ' [2] Debito\n'
                ' [3] Crédito: '
                ''))
print('')

if forma_pagamento == 1:
    saldo = produto - (produto * 0.1)
    print('Pagamentos À VISTA recebem um desconto de 10%: ')
    print('O valor a ser pago é R${:.2f}'.format(saldo))

elif forma_pagamento == 2:
    saldo = produto - (produto * 0.05)
    print('Pagamentos no DEBITO recebem um desconto de 5%:')
    print('O valor a ser pago é R${:.2f}'.format(saldo))

elif forma_pagamento == 3:
    forma_pagamento = int(input('Quantidade de parcelas: '))
    if forma_pagamento <= 2:
        saldo = produto
        parcela = saldo / 2
        print('O valor a ser pago é {}x de R${:.2f}'.format(forma_pagamento, parcela))
        print('O valor total do produto é de R${:.2f}'.format(saldo))
    elif 3 <= forma_pagamento:
        saldo = produto + (produto * 0.2)
        parcela = saldo / forma_pagamento
        print('O valor a ser pago é {}x de R${:.2f}'.format(forma_pagamento, parcela))
        print('Pagando um total de R${:.2f} no final'.format(saldo))
else:
    print('\033[31mOPÇÃO INVÁLIDA!\033[m')
