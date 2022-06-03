from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''
  Opções:
[ 0 ] Pedra
[ 1 } Papel
[ 2 ] Tesoura
Sua jogada? 
'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)
print('-=' * 9)
print('Eu joguei {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 9)

if computador == 0:  #COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('EU VENCI')

elif computador == 1:  #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('EU VENCI')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU')

elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('EU VENCI')
    elif jogador == 2:
        print('EMPATE')

else:
    print('JOGADA INVÁLIDA')