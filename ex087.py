# Aprimore o exercício anterior mostrando no final:
#A soma dos valores pares digitados
#a soma dos valores da terceira coluna
#o valor da segunda linha

matriz = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
pares = 0
for v in range(0, 3):
    for h in range(0, 3):
        matriz[v][h] = int(input(f'Informe o valor para posição [{v}, {h}]: '))
        if matriz[v][h] % 2 == 0:
            pares += matriz[v][h]
coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
linha = matriz[1][0] + matriz[1][1] + matriz[1][2]
'''        if matriz[0[]]
for c in matriz:
    for c in range(0, 3):
        coluna += matriz[0[2]]'''
print('-=' * 30)
for v in range(0, 3):
    for h in range(0, 3):
        print(f'[{matriz[v][h]:^5}]', end='')
    print()
print('-=' * 30)
print(f'Soma dos valores pares da matriz é: {pares}')
print(f'A soma da terceira coluna é: {coluna}')
print(f'E a soma dos valores da segunda linha é: {linha}')