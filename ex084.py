#Programa que leia nome e peso de várias pessoas guardando em uma lista e mostre:
#Quantas pessoas foram cadastradas
#Uma lista com as pessoas mais pesadas
#Uma lista com as pessoas mais leves
base_dados = list()
user = list()
total_users = 0
pesadas = list()
leves = list()
cont = 0
while True:
    user.append(str(input('Nome: ')).strip().title())
    user.append(float(input('Peso: ')))
    total_users += 1
    base_dados.append(user[:])
    user.clear()
    for users in base_dados:
        if cont == 0:
            pesadas = users[0]
            leves = users[0]
            print(users[:][1])
            print(pesadas, leves)
        else:
            if users[:][1] > users[:][1]:#Errado
                pesadas = users[0]
            if users[:][1] < users[:][1]:#Errado
                leves = users[0]
        cont += 1
    continuar = str(input('Deseja fazer um novo cadastro? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Por favor, Informe uma opção válida: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total de pessoas cadastradas foram {len(base_dados)}')
print(f'As pessoas mais pesadas são {pesadas}')
print(f'As mais leves são {leves}')

