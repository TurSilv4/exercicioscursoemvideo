lista = []
continuar = ''
while True:
    user_num = int(input('Digite um valor: '))
    if user_num in lista:
        print('O numero já está na lista... Digite um numero diferente: ')
    else:
        lista.append(user_num)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'O números dígitados são \n{sorted(lista)}')
