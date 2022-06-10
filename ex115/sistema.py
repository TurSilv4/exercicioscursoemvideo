from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'BasedeDados.txt'

# PROGRAMA PRINCIPAL
if not arquivoExiste(arq):  # Verifica se o arqivo existe
    criarArquivo(arq)  # Cria o arquivo
while True:
    user = menu(['Ver pessoas cadastradas', 'Novo cadastro', 'Sair do Sistema'])
    if user not in range(1, 4):
        print('\033[0;31mERRO: Digite uma opção válida\033[m')
        continue
    if user == 1:  # Mostra a lista
        lerArquivo(arq)
    elif user == 2:  # Adiciona pessoas a lista
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title()
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)
    else:  # Encerra
        cabeçalho('ENCERRANDO SISTEMA... ATÉ LOGO!')
        break
    sleep(2)
