# Criar um programa que ajude um jogador da mega sena a criar palpites o programa deve:
# Perguntar quantos jogos serão gerados e sortear 6 numeros entre 1 e 60 p cada jogo e.
# Registra-los em uma lista composta

from random import randint
from time import sleep
jogos = list()
random_numbers = list()
user = int(input('Quantos jogos serão gerados? ')) # quantidade de jogos
print(f'{user} Jogos registrados! \nGerando palpites...')
sleep(2)
for cont in range(0, user):
    random_numbers = [randint(1, 60) for x in range(6)] # gera os palpites na quantidade designada
    jogos.append(random_numbers[:])
    random_numbers.clear()
for j in range(0, user):
    print(f'{j+1}° jogo: {jogos[j]}')
    sleep(1)
