from datetime import date
ano = int(input('{}Que ano quer analizar? \n '
                '"Digite 0 para analizar a data atual":{} '.format('\033[34m', '\033[m')))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:       # != SINAL DE DIFERENTE
    print('\033[32mO ano {} é um ano Bissexto.\033[m'.format(ano))

else:
    print('\033[31mO ano {} não é bissexto\033[m'.format(ano))
