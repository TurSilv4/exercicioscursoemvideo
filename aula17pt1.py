num = [2, 5, 9, 1, 9]

# LISTAS PODEM SER MULTAVEIS
num[2] = 3
print(num)

# ADICIONAR NOVOS VALORES A LISTA
num.append(9)
print(num)

# DEIXA EM ORDEM
num.sort()
print(num)

# INVERTE A ORDEM DA LISTA
num.sort(reverse=True)
print(num)

print(f'Essa lista tem {len(num)} elementos')

# INSERE UM VALOR NOS POSIÇÃO DESIGNADA
num.insert(2, 0)
print(num)

# SE NÃO FOR INSERIDO VALOR É ELIMINADO O ULTIMOS VALOR DA LISTA, SENÃO ELIMINA O VALOR DESIGNADO
num.pop(2)
print(num)

# SE EXISTIR VARIOS VALORES IGUÁIS, É REMOVIDO APENAS O PRIMEIRO VALOR QUE APARECE
num.remove(9)
print(num)

# NUMEROS QUE NÃO ESTÃO NA LISTA DA ERRO
if 4 in num:
    num.remove(4)
else:
    print('Não achei o valor informado na lista')
print(num)

valores = list() or []

valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

for con in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
print(valores)

# CÓPIA DE LISTA
a = [2, 3, 4, 7]
b = a # DESSA FORMA VAI HAVER UM LIGAÇÃO ENTRE A LISTA A E B (UMA ALTERANDO A OUTRA)
b = a[:] # A LISTA B VAI RECEBER TODOS OS ELEMENTOS DA LISTA A (ASSIM NÃO ALTERA SEUS VALORES)
b[2] = 8
print(f'LIsta A: {a}')
print(f'Lista B: {b}')
