r1 = float(input('{}Primeiro valor:{} '.format('\033[34m', '\033[m')))
r2 = float(input('{}Segundo valor:{} '.format('\033[35m', '\033[m')))
r3 = float(input('{}Terceiro valor:{} '.format('\033[36m', '\033[m')))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Dado os valores {}, {}, {}. \n '
          'Seu triangulo {}PODE{} existir.'.format(r1, r2, r3, '\033[32m', '\033[m'))
else:
    print('Dado os valores {}, {}, {}. \n '
          'Seu triangulo {}NÃO PODE{} existir.'.format(r1, r2, r3, '\033[31m', '\033[m'))
