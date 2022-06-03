# EU (NÂO CONSEGUI)
'''fatorial = int(input('Digite o número que deseja fatorar: '))
resultado = 0
while 1 < fatorial:
for n in range(fatorial, 0, -1):
    resultado += fatorial * n
    print(resultado)'''

# UTILIZANDO MODULOS
'''numero = int(input('Digite um numero: '))
resultado = factorial(numero)
print('O fatorial de {} é {}'.format(numero, resultado))
'''
# UTILIZANDO O WHILE
'''numero = int(input('Digite um numero: '))
contador = numero
fatorial = 1
print('O resulado de {}! = '.format(numero), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)'''

# ULTILIZANDO O FOR
numero = int(input('Digite um numero: '))
resultado = 1
for c in range (numero, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    resultado *= numero * c
print(resultado)
