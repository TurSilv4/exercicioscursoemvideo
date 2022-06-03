print('=-' * 20)
print('{:^40}'.format('''CADASTRO DE PESSOAS'''))
print('=-' * 20)
media = 0
hv = 0
m = 0
for p in range(1, 5):
    nome = str(input('Nome: ')).strip().title().split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).upper()
    print('-' * 40)
    media += idade
    if sexo == 'm':
        if idade > hv:
            hv = idade
            mv = nome
    elif sexo == 'f':
        if idade < 20:
            m += 1
print('O homem mais velho é o {} com {} anos.'.format(mv[0], hv))
print('')
print('{} mulheres tem menos de 20 anos.'.format(m))
print('')
print('A media de idade do grupo é {:.1f} anos.'.format(media / p))
