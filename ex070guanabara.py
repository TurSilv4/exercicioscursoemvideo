total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço >= 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é R${total:.2f}')
print(f'{totmil} custaram mais que R1000.00')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')
print('Acabou')
