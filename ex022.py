nome = str(input('Nome completo: ')).strip()

print('Seu nome em maiúsculas {}.'.format(nome.upper()))

print('Seu nome em minúsculas {}.'.format(nome.lower()))

print('O nome tem ao todo {} letras.'.format(len(nome) - (nome.count(' '))))
'''print('O nome tem ao todo {} letras.'.format_map(len(nome.replace(' ', ''))))'''

s = nome.split()

print('Seu primeiro nome é {} e tem {} letras.'.format(s[0], len(s[0])))
