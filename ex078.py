valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    maior = max(valores)
    menor = min(valores)
posicao_maior = valores.count(maior)
posicao_menor = valores.count(menor)

print(f'Dado os valores {valores}...')
print(f'O maior é o numero {maior} na posição {valores.index(maior)}...')
print(f'O menor é o numero {menor} na posição {valores.index(menor)}...')
