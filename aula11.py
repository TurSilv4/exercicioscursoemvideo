print('\033[7;40mOlá mundo!\033[m')         #DESORGANIZADO

nome = 'Arthur'

print('Olá! muito prazer em te conhecer {}{}{}'.format('\033[4;36m', nome, '\033[m)')) #USANDO .FORMAT (MAS ORGANIZADA)

                                                #DICIONÁRIO
cores = {'azul': '\033[34m',
         'vermelho': '\033[41m',
         'PeB': '\033[7;40m',
         'limpa': '\033[m'}

print('Olá! Muito prazer em te conhecer {}{}{}'.format(cores['PeB'], nome, cores['limpa']))
