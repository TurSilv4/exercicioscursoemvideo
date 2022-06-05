# Criar um programa que tenha uma função fatorial() que receba dois parametros :
# O primeiro que indique o numero a calcular e o outro chamado show, que tera um valor True or False
# Indicando se sera mostrado ou não na tela de processo de cálculo do fatorial


def fatorial(num, show=bool(input('Ver resolução? True/False'))):
    f = 1

    for cont in range(num, 0, -1):
        f *= cont
    if show == True:
        for cont in range(num, 0, -1):
            print(cont, end=' x 'if cont > 0 else)
        print(' = ', end='')
    return f


n = int(input('Qual número deseja calcular? '))
r = fatorial(n)
print(r)
