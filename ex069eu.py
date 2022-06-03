print('-' * 20)
print('{:^20}'.format('''CADASTRO'''))
print('-' * 20)
idade = quant = quant_maior = homem = quant_menor = 0
sexo = continuar = ''

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    quant += 1
    if idade >= 18:
        quant_maior += 1
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff':
        if idade <= 20:
            quant_menor += 1
    continuar = str(input('Deseja fazer um novo cadastro? [S/N]'))

    while continuar not in 'SsNn':
        continuar = str(input('Deseja fazer um novo cadastro? [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
    print('-' * 40)
print('-' * 40)
print(f'Ao todo foram cadastrados {quant} pessoas, Das quais: ')
print(f'{quant_maior} eram maiores de idade')
print(f'{homem} eram homens')
print(f'{quant_menor} mulheres tem menos de 20 anos')
