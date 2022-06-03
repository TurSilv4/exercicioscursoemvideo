n = str(input('Digite seu nome completo: ')).strip()
nm = n.title()
lista = nm.split()

print('Olá, muito prazer.')
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}.'.format(lista[len(lista) - 1]))
