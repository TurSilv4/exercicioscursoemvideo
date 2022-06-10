from ex115.lib.interface import cabeçalho

def arquivoExiste(nome):
    """Verifica se um arquivo .txt existe"""
    try:
        a = open(nome, 'rt')  # Abre o arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    """Cria um arquivo .txt"""
    try:
        a = open(nome, 'wt+')  # Cria um arquivo de texto
        a.close()
    except:
        print('Houve um erro na criaçao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    """Mostra o arquivo"""
    try:
        a = open(nome, 'rt')  # Abre/Lê o arquivo
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        c = 1
        print(f'\033[0;36m{"No."}  {"Nome":<27}{"Idade"}\033[m')
        for linha in a:  # Mostra a lista
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'\033[0;33m{c:2}\033[m - {dado[0]:<27}{dado[1]} anos')
            c += 1
    finally:
        a.close()  # Fecha o arquivo


def cadastro(arquivo, nome='desconhecido', idade=0):
    """Adiciona um novo cadastro ao arquivo"""
    try:
        a = open(arquivo, 'at')  # a == append/ t == text (adiciona arquivo de texto)
    except:
        print('\033[0;31mHouve um erro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mHouve um problema ao adicionar novos usuários\033[m')
        else:
            print('-' * 40)
            print(f'\033[0;32mNovo registo de {nome} adicionado com sucesso\033[m')

