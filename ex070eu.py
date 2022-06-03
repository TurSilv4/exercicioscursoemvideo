print('-' * 31)
print('{:^31}'.format('''Silva's Store'''))
print('-' * 31)
preco = total = maior_1000 = mais_barato = cont = 0
continuar = npmb = produto = ''
while True:
    produto = str(input('Nome do produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco >= 1000:
        maior_1000 += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        npmb = produto

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar in 'Nn':
        break


print(f'Total a pagar R${total:.2f}')
print(f'{maior_1000} produtos custam mais que R$1000,00 ')
print(f'O produto mais barato é {npmb} custando R${mais_barato:.2f}')