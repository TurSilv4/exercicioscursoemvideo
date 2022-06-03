'''Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista,
ja na posição de inserção(sem usar o .sort())
e mostr-os na tela em ordem'''

lista = []
for cont in range(0, 5):
    user = int(input('Digite um valor: '))
    if cont == 0 or user > lista[-1]:
        lista.append(user)
    else:
        pos = 0
        while pos < len(lista):
            if user <= lista[pos]:
                lista.insert(pos, user)
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')
