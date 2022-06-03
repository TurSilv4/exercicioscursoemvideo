nome = str(input('Qual seu nome? ')).title().strip()
                                        #ESTRUTURA CONDICIONAL ANINHADA
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino!')
else:
    print('Que bosta de nome heim irmão!')

print('Tenha um bom dia, {}!'.format(nome))
