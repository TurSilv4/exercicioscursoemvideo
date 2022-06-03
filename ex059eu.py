escolha = 'S'
menu = 0
maior_valor = 0
resultado = 0
valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))
while menu != 5:
    print('=-' * 12)
    print('{:^24}'.format('''MENU'''))
    print('=-' * 12)
    menu = int(input(
'''[ 1 ] Soma.
[ 2 ] Multiplicação.
[ 3 ] Informar o maior.
[ 4 ] Digitar novamente.
[ 5 ] Sair.
>>>> Sua opção: '''))
    if menu == 1:
        resultado = valor_1 + valor_2
        print('A soma dos valores é {}'.format(resultado))
        print('')
    elif menu == 2:
        resultado = valor_1 * valor_2
        print('A multiplicação dos valores é {}'.format(resultado))
        print('')
    elif menu == 3:
        maior_valor = valor_1
        if valor_1 > valor_2:
            resultado = valor_1
            print('O primeiro valor {} é o maior'.format(resultado))
        elif valor_2 > valor_1:
            resultado = valor_2
            print('O segundo valor {} é o maior'.format(valor_2))
        else:
            print('Ambos valores são iguais')
    elif menu == 4:
        valor_1 = int(input('Digite um novo valor: '))
        valor_2 = int(input('Digite outro valor: '))
    elif menu > 5:
        print('Opção inválida!')
        print('')
    escolha = str(input('Voltar ao MENU? [S/N] ')).upper().strip()
    if escolha == 'N':
        menu = 5
