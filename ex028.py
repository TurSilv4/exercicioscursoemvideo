from random import randint
from time import sleep

'''n = int(input('Tente advinhar em que numero eu estou pensando de 0 a 5: '))
r = randint(0, 5)

if n == r:
    print('Parabens você acertou!\n Eu tanbém pensei no numero {}.'.format(r))

else:
    print('Você errou. \n Eu pensei no numero {} \n Tente denovo HAHAHA.'.format(r))
'''

computador = randint(1, 5) # Faz o PC "pensar" em um numero.
print('\033[33m-=-' * 20)
print('\033[36mVou "pensar" em um numero de 0 a 5. Tente advinhar...')
print('\033[33m-=-' * 20)
jogador = int(input('\033[36mEm que numero eu pensei? ')) # Jogador tenta advinhar
print('\033[34mHUUUM...')
sleep(2)
if jogador == computador:
    print('\033[32mPARABENS! Você acertou!')
else:print('\033[31mBEEEN! Você errou. EU pensei no número {} HEHEHE...'.format(computador))