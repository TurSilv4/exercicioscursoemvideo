n1 = int(input('{}Primeiro valor:{} '.format('\033[34m', '\033[m')))
n2 = int(input('{}Segundo valor:{} '.format('\033[35m', '\033[m')))
n3 = int(input('{}Terceiro valor:{} '.format('\033[36m', '\033[m')))

cor = {'maior': '\033[32m',
       'menor': '\033[31m',
       'limpar': '\033[m'}

#VERIFICANDO QUEM É MENOR:
menor = n1

print('')

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n2 and n3 < n1:
    menor = n3

print('O {} MENOR {} valor é {}'.format(cor['menor'], cor['limpar'], menor))

#VERIFICANO QUEM É MAIOR:

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print('O {} MAIOR {} valor é {}'.format(cor['maior'], cor['limpar'], maior))
