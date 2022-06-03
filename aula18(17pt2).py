teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste) #['Gustavo', 40]

galera = list()
galera.append(teste[:]) # Se usado um "append(teste)" é criado uma ligação, alterando assim as duas listas (Necessário fazer uma cópia de lista [:] )
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera) # [['Maria', 22], ['Maria', 22]]

galera = [['João', 17], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # Uma estrutura contem várias outras estruturas dentro de sá
print(galera) # Mostra todos os dados
print(galera[0]) # Mostra só a estrutura [0] da lista sendo: ['João', 17]
print(galera[0][0]) # Mostra apenas o "Valor" [0] dentro da estrutura [0] da lista sendo: ['João']
print(galera[2][1]) # [13]

for p in galera:
    print(p) # Faz uma lista com os valores
    print(p[0]) # Apenas os nomes
    print(p[1]) # Apenas as idades
    print(f'{p[0]} tem {p[1]} anos de idade') # [X] pessoa tem [x] anos de idade

galera = list()# Estrutura principal
dado = list()# Estrutura auxiliar
for c in range(0, 3):
    dado.append(str(input('Nome: '))) #Recolhe dados em uma lista
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Adiciona os dados em outra lista (Lembras de fazer uma copia da lista)
    dado.clear() # Limpa a lista de dados
print(galera)

# Filtro para mostrar apensa as pessoas com mais de 21 anos
maior = menor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de 21 anos')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores')
