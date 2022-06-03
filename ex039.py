from datetime import date
print('\033[32m=\033[33m-' * 16)
print('\033[34mAnálise de alistamento mílitar.')
print('\033[32m=\033[33m-\033[m' * 16)

sexo = int(input('''Indique o sexo:
[ 1 ] Masculino
[ 2 ] Feminino
'''))
print('')

if sexo == 1:
    nasc = int(input('Em que ano você nasceu? '))
    data = date.today().year
    idade = data - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, data))
    if idade == 18:
        print('Você deve se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o seu alistamento!'.format(saldo))
        ano = data + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado {} anos atrás'.format(saldo))
        ano = data - saldo
        print('Seu alistamento foi em {}'.format(ano))
elif sexo == 2:
    print('O seu alistamento não é obrigatorio')
else:
    print('VALOR INVÁLIDO, DIGITE NOVAMENTE')

#MEU MODELO
'''if data - ano < 18:
    ano = data - ano - 18
    print('\033[mAinda faltam {} anos para ter de se alistar.'.format(ano))
elif data - ano == 18:
    print('DIN DIN DIN!! Esta na hora de fazer seu alistamento.')
else:
    ano = data - ano - 18
    print('Você esta {} anos atrasado.'.format(ano))'''
