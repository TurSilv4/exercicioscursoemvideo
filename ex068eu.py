from random import randint

print('=-' * 15)
print('Vamos brincar de Par ou Impar? ')
print('-=' * 15)
resultado = cont = 0
i_p = ''
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    i_p = str(input('Par ou Ímpar? [P/I] ')).strip().upper()# Impar ou Par
    while i_p not in 'IiPp':
        i_p = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-' * 30)
    resultado = jogador + computador
    print('Deu PAR'if resultado % 2 == 0 else 'Deu IMPAR', end=' ')
    print(f'Voce pensou em {jogador} \nEu pensei em {computador} \nIsso da {resultado}')
    print('-' * 30)
    if i_p == 'P':
        if resultado % 2 == 0:
            cont += 1
            print('Você ganhou')
        else:
            print('Voce perdeu!')
            print(f'Suas vitórias são: {cont}')
            break
    elif i_p == 'I':
        if resultado % 2 != 0:
            print('Voce ganhou!')
            cont += 1
        else:
            print('Você perdeu!')
            print(f'Suas vitórias são: {cont}')
            break
    print('-' * 30)