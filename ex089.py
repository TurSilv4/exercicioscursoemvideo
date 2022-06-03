# Criar um programa que leia nome e nota de varios alunos e guarde tudo em uma lista composta:
# No final mostrar um boletim com a média de cada um e permitir o usuario  veja a nota individual de cada aluno

data = list()
cadastro = list()
user = list()
cont = 0
encerrar = 999
while True:
    cadastro.append(str(input('Nome: ')).strip().title())
    for nota in range(1, 3):
        user.append(int(input(f'Nota {nota}: ')))
    cadastro.append(user[:])    #Adicona a nota a lista dos nomes
    user.clear()                #Limpa a lista
    data.append(cadastro[:])    #Adiciona os nomes a lista de todos os dados
    cadastro.clear()            #Limpa  lista de nomes
    cont += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Informe uma opção válida: [S/N] ')).strip().upper()[0]
    print('-' * 30)
    if continuar == 'N': #Encerra laço de cadastros
        break
c = 0 #Contador
print('=-' * 30)
print('No.  NOME        MÉDIA') #Boletim
print('-' * 22)
for aluno in data:
    media = (aluno[1][0] + aluno[1][1]) / 2         #Calcula a média
    print(f'{c+1:^3}  {aluno[0]:<12} {media:.1f}')  #Mosrta N° Nome e media dos alunos
    c += 1
while True: #Laço de notas individuais
    print('=-' * 30)
    encerrar = int(input('Deseja ver as notas de qual aluno? '))
    if encerrar == 999:
        print('PROGRAMA ENCERRANDO...\n VOLTE SEMPRE!')
        break
    else:
        print(f'O aluno(a): {data[encerrar-1][0]} tirou as notas {data[encerrar-1][1][:]}\n')

# Deu um trampinho
