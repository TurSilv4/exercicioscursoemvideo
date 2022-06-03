n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
cor = {'vermelho':'\033[31m',
       'verde':'\033[32m',
       'roxo':'\033[35m',
       'azul':'\033[34m',
       'ciano':'\033[36m',
       'limpa':'\033[m'}
print('')

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print('{}O tipo do triângulo é "EQUILÁTERO".{}'.format(cor['verde'], cor['limpa']))
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print('{}O tipo do triângulo é "ISÓCELES"{}'.format(cor['azul'], cor['limpa']))
    else:
        print('{}O tipo do triângulo é "ESCALENO"{}'.format(cor['roxo'], cor['limpa']))
else:
    print('{}O triângulo não pode existir{}'.format(cor['vermelho'], cor['limpa']))
