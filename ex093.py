#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome e quantas partidas o jogador jogou. Depois vai ler a quantidade de gols em cada partida.
#No final de tudo isso será quardado em uma dicionario, incluindo o total de gols feitos durante o campeonato

data = dict()
gols = list()
total_gols = 0
data['Nome'] = str(input('Nome: ')).strip().title()
partidas = int(input('Quantas partidas jogadas: '))
for c in range(0, partidas):
    user = int(input(f'Quantos gols na partida {c}: '))
    gols.append(user)
    total_gols += user # Pode usar tbm sum(data['Gols']) pra somar todos os valores
data['Gols'] = gols[:]
data['Total de gols'] = total_gols
def linha():
    print('=-' * 30)


linha()
print(data)
linha()
for k, v in data.items():
    print(f'O campo {k} tem valor {v}')
linha()
print(f'O jogador {data["Nome"]} jogou {partidas} partidas')
for cont, v in enumerate(data['Gols']):
     print(f'    => Na partida {cont}, fez {v} gols')
print(f'Foi um total de {total_gols} gols.')
