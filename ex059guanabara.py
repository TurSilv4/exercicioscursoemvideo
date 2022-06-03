from time import  sleep
valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
opcao = 0
resultado = 0
while opcao != 5:
    print('=-' * 10)
    print('{:^20}'.format('''MENU'''))
    print('=-' * 10)
    print('''[ 1 ] SOMA
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR VALOR
[ 4 ] NOVOS VALORES
[ 5 ] SAIR ''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        resultado = valor_1 + valor_2
        print('A soma entre {} + {} é {}'.format(valor_1, valor_2, resultado))
    elif opcao == 2:
        resultado = valor_1 * valor_2
        print('O resultado de {} x {} é {}'.format(valor_1, valor_2, resultado))
    elif opcao == 3:
        if valor_1 == valor_2:
            print(' Os dois valores são iguais')

        elif valor_1 > valor_2:
            resultado = valor_1
        else:
            resultado = valor_2
        print('Entre {} e {} o maior valor é {}'.format(valor_1, valor_2, resultado))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        valor_1 = int(input('Informe um novo valor: '))
        valor_2 = int(input('Informe outro valor: '))
    elif opcao == 5:
        sair = str(input('Tem certeza que deseja sair? [S/N]')).strip().upper()
        if sair == 'S':
            opcao = 5
    else:
        print('Opção inválida. Escolha novamente.')
    print('FINALIZANDO...')
    sleep(1)
    print('=-' * 15)
    print('Fim do programa... Volte sempre!')

