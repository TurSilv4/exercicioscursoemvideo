# Criar um programa que tenha uma função fatorial() que receba dois parametros :
# O primeiro que indique o numero a calcular e o outro chamado show, que tera um valor True or False
# Indicando se sera mostrado ou não na tela de processo de cálculo do fatorial


def fatorial(num, show=False):
    f = 1

    for cont in range(num, 0, -1):
        f *= cont
    if show:
        for cont in range(num, 0, -1):
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
    else:
        return print(f'O resultado de {num}! é {f}')

n = int(input('Qual número deseja calcular? '))
resolução = bool(input('Digite SIM se deseja ver a resolução: [Ignore para não] '))
r = fatorial(n, resolução)
print(r)
print('-' * 30)
