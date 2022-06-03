pessoas = {'nome': 'gustavo', 'sexo': 'm', 'idade': 22}
print(pessoas['sexo'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #Usar aspas duplas quando estiver em um print(se n da erro)

print(pessoas.keys()) #Mostra as chaves (NOme, sexo, idade) sem os valores

print(pessoas.values()) #Mostra apenas os valores das chaves (todos)

print(pessoas.items()) #Mostra todos os itens(Uma lista com 3 tuplas)

for k, v in pessoas.items(): #Mostra as chaves e os valores('Nome = Gustavo')
    print(f'O {k} = {v}')    #Nos dicionarios não tem o 'enumerate' é nescessario usar o .items

del pessoas['sexo'] #Deleta a chave 'sexo' e seu (ou seus) valores
print(pessoas)

pessoas['nome'] = 'leandro' #Troca o nome 'gustavo' por 'leandro'

pessoas['pesso'] = 98,5 #Adiciona uma nova chave no dicionario com mseu valor(não é necessario dar .append)

#Dicionario dentro de lista
brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf']) #Elemento 0 (estado1) - na chave 'uf' - print(Rio de Janeiro)
print(brasil[1]['sigla']) #Elemento 1 (estado 2) - na chave 'sigla' - print(SP)

estado = dict()
br = list()
for c in range(0, 3):
    estado['uf'] = str(input('Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    br.append(estado.copy()) #Diconarios não funciona o fatiamento de itens tem de ser usado o .copy
for e in br: #Para cada item da lista (Dicionario)
    for k, v in e.items(): #Para cada valor no Dicionario
        print(f'A chave {k} tem valor {v}') # Print(A chave 'uf' tem valor 'São paulo'/ a chave ' sigla' tem valor 'SP')
#ou
    for v in e.values(): # Mostra todos os valores em ordem
        print(v, end='-') # print(São paulo - SP/ Rio de Janeiro - RJ) etc..

