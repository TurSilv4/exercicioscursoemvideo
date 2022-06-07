# Crie um programa que tenha uma função leiaInt(), que vai funcionar semelhante a função input(),
# Só que fazendo uma validação pra aceitar apenas numeros


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Informe uma valor inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Vocẽ digitou o número {n}')
