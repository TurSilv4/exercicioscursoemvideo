'''nome = input('Nome da cidade: ')
n1 = nome.title()
d = n1.split()
nome2 = 'Santo' or 'Santa' in d[0]

if nome2:
    var = True
    print('Sim, {} começa com a palavra "Santo".'.format(nome))
else:
    print('Não, o nome da cidade não começa com "Santo".')'''

nome = str(input('Nome da cidade: ')).strip().upper()
print('SANTO' in nome[:5])
