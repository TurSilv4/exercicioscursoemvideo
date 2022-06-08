# Re-escreva a função leiaInt() do ex104, incluindo agora a possibilidade de digitalização de um numero de tipo invalido.
# Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mO valor informado é inválido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO Usuario preferiu não informar o valor!\033[m')
            return 0
        else:
            return n



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mO valor informado é inválido!\033[m')
        except KeyboardInterrupt:
            print('\033[0;31m\nO usuario preferiu não informar esse numero\033[m')
            return 0
        else:
            return n
