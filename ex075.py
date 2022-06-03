numeros = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
total = numeros
print(f'Os valores digitados são: {numeros}')


print(f'Apareceram {numeros.count(9)} vezes o numero 9')
if 3 in numeros:
    print(f'O numero 3 apareceu a primeira vez na {numeros.index(3)+1}° posição')
else:
    print('Não há o numero 3 na lista')
print('Os valores pares são : ',end='')
for par in numeros:
        if par % 2 == 0:
            print(par, end=' ')
