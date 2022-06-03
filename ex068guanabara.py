from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] '))[0]
    print(f'Você jogou {jogador} e eu joguei {computador}. Total de {total}')
    print('Deu PAR'if total % 2 == 0 else 'Deu IMPAR', end=' ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER... Você venceu {v} vezes')
