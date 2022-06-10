def linha():
    print()
    print('\033[7;40m \033[m' * 40)


def leiaInt(str):
    while True:
        try:
            user = int(input(str))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor informe um valor inteiro válido.\033[m')
        except KeyboardInterrupt:
            return 0
        else:
            return user


def cabeçalho(txt):
    print()
    print(f'\033[7;40m{txt.center(40)}\033[m')
    print()


def menu(lista):
        cabeçalho('MENU PRINCIPAL')
        for c, item in enumerate(lista):
            print(f'\033[0;33m[ {c+1} ] \033[0;34m{item}\033[m')
        print('-' * 40)
        user = leiaInt('\033[0;33mSua opção: \033[m')
        return user
