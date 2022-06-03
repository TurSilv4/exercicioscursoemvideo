'''nome = str(input('Qual seu nome? ')).strip()

if nome == 'Arthur':
    print('Aí sim hein garotão!.')
#                                            CONDIÇÃO SIMPLES

else:
    print('Que belo nome hein meninão.')
#                                            CONDIÇÃO COMPOSTA
print('Bom dia, {}.'.format(nome))
'''

n1 = float(input('1° Bimestre: '))
n2 = float(input('2° Bimestre: '))
n3 = float(input('3° Bimestre: '))
n4 = float(input('4° Bimestre: '))

m = (n1 + n2 + n3 + n4) / 4

print('Sua media foi {:.1f}'.format(m))
if m >= 5:
    print('PARABENS! Você foi aprovado.')

else:
    print('SINTO MUITO! Mas você foi reprovado.')
