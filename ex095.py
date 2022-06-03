gols = list()
data = dict()
jogadores = list()
total_gols = 0
encerrar = 0
def linha():
    print('-' * 40)


while encerrar != 999:
    while True:
        data['Nome'] = str(input('Nome: ')).strip().title()
        partidas = int(input(f'Quantas partidas {data["Nome"]} jogou: '))
        for c in range(0, partidas):
            user = int(input(f'Quantos gols na partida {c}: '))
            gols.append(user)
        data['Gols'] = gols[:]
        total_gols = sum(data['Gols'])
        data['Total de gols'] = total_gols
        total_gols = 0
        gols.clear()
        jogadores.append(data.copy())
        data.clear()

        laço = str(input('Deseja fazer um novo cadastro? [S/N]')).strip().upper()[0]
        while laço not in 'SN':
            laço = str(input('Informe uma opção válida: [S/N]')).strip().upper()[0]
        linha()
        if laço == 'N':
            break
    linha()
    print('Cod', end='')
    for i in jogadores:
        for s in i.keys():
            print(f'{s:<15}', end='')
    print()
    linha()
    for c, v in enumerate(jogadores):
        print(f'{c:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
    print()
    linha()
    print(jogadores)
    linha()
    encerrar = int(input('Deseja verificar os dados de qual jogador? [999 para ENCERRAR] '))
