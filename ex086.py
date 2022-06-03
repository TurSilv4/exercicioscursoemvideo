# Crie um programa que crie uma matriz da dimensão 3x3 e prencha com os valores lidos no teclado
# No final mostre a matriz na tela com o formação correta

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for v in range(0, 3):
    for h in range(0, 3):
        matriz[v][h] = int(input(f'Informe o valor para posição [{v}, {h}]: '))
print('-=' * 30)
for v in range(0, 3):
    for h in range(0, 3):
        print(f'[{matriz[v][h]:^5}]', end='')
    print()
