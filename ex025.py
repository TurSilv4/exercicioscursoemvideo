'''n1 = input('Nome completo: ')
n2 = n1.title()
n3 = 'Silva' in n2

if n3:
    var = True
    print('Sim, {}, possui "Silva" em seu nome.'.format(n1))
else:
    print('Não, {}, não possui "Silva" em seu nome.'.format(n1))'''

nome = str(input('Nome completo: ')).strip().title()
print('Seu nome tem "Silva" {}.'.format('Silva'in nome))

