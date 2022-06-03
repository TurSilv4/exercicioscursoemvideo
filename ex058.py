from random import randint
# EU
'''print('\033[33m-=-' * 20)
print('\033[36mVou "pensar" em um numero de 0 a 5. Tente advinhar...')
print('\033[33m-=-\033[m' * 20)
jogador = 0
computador = randint(1, 10)
quantia_jogadas = 0
while computador != jogador:
    numero = int(input('Em que número estou pensado? '))
    jogador = numero
    if jogador != computador:
        quantia_jogadas += 1
        print('BEEN! Você errou! \n Tente novamente')
        print('')
    elif jogador == computador:
        quantia_jogadas += 1
        print('Parabens! Você acertou em {} jogadas'.format(quantia_jogadas))
        print('')
        print('Pensei no numero {}'.format(computador))'''
# GUANABARA

print('Vou pensar em um numero. Quero ver você tentar descobrir...')
print('De 0 a 10...')
computador = randint(1, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente novamente.')
        else:
            print('MENOS... Tente novamente.')
print('Parabens você acertou em {} palpites'.format(palpite))
