# Crie um programa que leia o nome, sexo e idade de varias pessoas guardando od em um dicionario, e todos os dicionarios em uma lista
# e Mostre: Quantas pessoas cadastradas; a media de idade; uma lista com mulheres; uma lista com idade a cima da media
pessoas = dict()
data = list()
pessoas_cadastradas = 0
soma = 0
def linha():
    print('-' * 30)


while True:
    pessoas['Nome'] = str(input('Nome: ')).strip().title()
    user = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while user not in 'MF':
        user = str(input('Por favor informe um valor válido: [M/F] ')).strip().upper()[0]
    pessoas['Sexo'] = user
    user = int(input('Idade: '))
    pessoas['Idade'] = user
    soma += user #Media
    data.append(pessoas.copy())
    pessoas.clear()
    pessoas_cadastradas += 1 #Pessoas cadastradas

    encerrar = str(input('Deseja fazer um novo cadstro? [S/N] ')).strip().upper()[0]
    while encerrar not in ('SN'):
        encerrar = str(input('Informe um valor válido: [S/N] ')).strip().upper()[0]
    linha()
    if encerrar == 'N':
        break
print(f'Temos {pessoas_cadastradas} pessoas cadastradas.')
print(f'A média de idade é {soma/pessoas_cadastradas:.1f}') #Media
print(f'As mulheres cadastradas são : ',end='')
for d in data:
    if d['Sexo'] == 'F':
        print(d['Nome'], end=', ')
print('\nAs pessoa com idade maior que a media são: ', end='')
for d in data:
    if d['Idade'] > soma / pessoas_cadastradas:
        print(d['Nome'], end=', ')
print('ENCERRANDO O PROGRAMA...')
