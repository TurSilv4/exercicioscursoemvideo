'''Criar um programa que lerá vários valores coloca-los em uma lista e dividi-los em outras duas listas;
uma de valores pares e outra de valores impares;
e mostrar o conteudo das tres listas no final'''
lista = []
par = []
impar = []
while True:
    user_num = int(input('Informe um valor: '))
    lista.append(user_num)
    if user_num % 2 == 0:
        par.append(user_num)
    else:
        impar.append(user_num)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Informe uma opção válida: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(f'A lista possui os valores {lista} \nSendo: \n Par: {par} \n Impar: {impar} ')
