# EU

cont = multiplicação = 0
print('-' * 34)
tabuada = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 34)

while True:
    if tabuada < 0:
        break
    for cont in range(1, 11):
        multiplicação = cont * tabuada
        print(f'{tabuada} x {cont:2} = {multiplicação:2}')
    print('-' * 34)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 34)
print('PRIGRAMA FINALIZADO. VOLTE SEMPRE!')


# GUANABARA

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrada. Volte sempre!')