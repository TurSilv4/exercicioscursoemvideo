from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print('Valores sorteados: ')
print('=' * 30)
for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)
for i, v in jogadores.items():
    print(f'O {i} tirou {v} no dado.')
    sleep(0.5)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=' * 30)
for i, v in enumerate(ranking):
    print(f'{i+1}°lugar: {v[0]} com {v[1]}')
    sleep(0.7)
