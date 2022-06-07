# Criar um programa que tenha uma função fatorial() que receba dois parametros :
# O primeiro que indique o numero a calcular e o outro chamado show, que tera um valor True or False
# Indicando se sera mostrado ou não na tela de processo de cálculo do fatorial


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um numero
    :param num: Recebe o valor a ser calculado
    :param show: (opcional) Mortrar ou nao a resoluçao da conta
    :return: O valor do Fatorial de num
    """
    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(f'{cont}', end='')
            print(' x ' if cont > 1 else ' = ', end='')
        f *= cont
    return f

n = int(input('Qual número deseja calcular? '))
resolução = bool(input('Digite SIM se deseja ver a resolução: [Ignore para não] '))
print(fatorial(n, resolução))
print('-' * 30)
help(fatorial)
