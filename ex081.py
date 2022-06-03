# Criar um prigramam que leia varios valores e coloque em uma lista, depois mostrar :

lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))

    cont += 1# ou da pra usar o len(lista)

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Escolha um valor válido: [S/N]'))
    if continuar == 'N':
        break
# A lista de valores ordenada em ordem decrescente:
lista.sort(reverse=True)
print(f'Foram digitados os números {lista}')

# Quantos numeros foram digitados:
print(f'A lista tem {cont} valores')

# Se o valor 5 foi digitados e esta ou não na lista:
print(f'O valor 5 está na lista na posição {lista.index(5)+1}'if lista.count(5) != 0 else 'O valor 5 não foi encontrado na lista!')
