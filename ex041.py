from datetime import date
print('\033[34m=-=' * 15)
print('\033[36mFEDERAÇÃO NACIONAL DE NATAÇAO\033[m')
print('\033[34m=-=' * 15)

idade = int(input('\033[mAno de nascimento do atleta: '))
data = date.today().year
cor = {'vermelho':'\033[31m',
       'verde':'\033[32m',
       'roxo':'\033[35m',
       'azul':'\033[34m',
       'ciano':'\033[36m',
       'limpa':'\033[m'}

if data - idade <= 9:
    print('Sua categoria é: \n {}MIRIM.{}'.format(cor['vermelho'], cor['limpa']))

elif data - idade <= 14:
    print('Sua categoria é: {}\n INFANTIL{}'.format(cor['verde'], cor['limpa']))
    
elif data - idade <= 19:
    print('Sua categoria é: {}\n JUNIOR{}'.format(cor['roxo'], cor['limpa']))
    
elif data - idade <= 25:
    print('Sua classificação é: {}\n SÊNIOR{}'.format(cor['azul'], cor['limpa']))
    
else:
    print('Sua clasificação é: \n {}MASTER{}'.format(cor['ciano'], cor['limpa']))
