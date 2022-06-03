media = 0
mhomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome:')).strip().split()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    media += idade / 4
    if p == 1 and sexo in 'Mm':
        mhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(mhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
