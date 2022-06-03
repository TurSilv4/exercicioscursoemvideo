#Criar um programa que leia sete valores e os separe entre pares e impares (mas utilizado uma unica lista)
#E no final mostre-a em ordem crecente


lista = []

for cont in range(0, 7):
    user = int(input(f'Informe o {cont+1}° Valor: '))
    lista.append(user)
print('Pares: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=', ')
print('Impares: ', end='')
for n in lista:
    if n % 2 != 0:
        print(n, end=', ')
# Não consegui colocar eles em ordem
