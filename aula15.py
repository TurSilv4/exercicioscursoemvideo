'''cont = 1
while cont < 11:
    print(cont)
    cont += 1
print('Acabou')'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
    s -= 999
print('A soma vale {}'.format(s))

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n'''
#print('A soma vale {}'.format(s)) # COMANDO ATE P3.6

# F STRING NOVO FORMATO P 3.6
#print(f'A soma vale {s}')

nome = 'Jose'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha {salario:.2f}')
