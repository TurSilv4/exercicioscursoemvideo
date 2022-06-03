n = int(input('Digite um numero: '))
print('''Escolha uma das bses para conversão
 [ 1 ] BINÁRIO
 [ 2 ] OCTAL
 [ 3 ] HEXADECIMAL''')
opção = int(input('Sua escolha:'))

if opção == 1:
    print('O numero {} em Binário é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('O numero {} em Octál é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('O numero {} em Hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida')