# Fazer programa com uma função escreva(), que recebe um texto qualquer como parametro e mostre
# uma mensagem com tamanho adapatativo

def mensagem(msg):
    t = len(msg)
    print('~' * (t + 4))
    print(f'{msg:^{t+4}}')
    print('~' * (t + 4))


mensagem('Ola Mundo!')
mensagem('Em um ninho de mafagafos havia sete mafagafinhos.')
mensagem('Stuart litle, melhor filme ever!')
