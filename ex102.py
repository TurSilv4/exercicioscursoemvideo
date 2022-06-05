# Criar um programa que tenha uma função fatorial() que receba dois parametros :
# O primeiro que indique o numero a calcular e o outro chamado show, que tera um valor True or False
# Indicando se sera mostrado ou não na tela de processo de cálculo do fatorial


def fatorial(num):
    f = 1

    for cont in range(num, 0, -1):
        f *= cont
    if show == True:
        for cont in range(num, 0, -1):
            print(f'{cont}')
        print(' + ' if cont > 0 else ' = ')
    return f


n = int(input('Qual número deseja calcular? '))
r = fatorial(n)
print(r)
