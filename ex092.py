#Crie um proograma que leia nome ano de nascimento e carteira de trabalho e os cadastre (com idade) em um dicionario
#se por acaso a CTPS for diferente de zero o dicionario recebera tembem o ano de contratação e o salario.
#Calcule e acrescente alem da idade cim quantos anos a pessoa ira se aposentar

from datetime import date
user = dict()

user['Nome'] = str(input('Nome: ')).strip().title()
ano_nascimento = int(input('Ano de nascimento: '))
user['Idade'] = date.today().year - ano_nascimento
user['CTPS'] = int(input('N° da CTPS: '))
if user['CTPS'] != 0:
    user['Ano de contratação'] = int(input('Ano de contratação: '))
    user['Salário'] = float(input('Salário: '))
    user['Aposentadoria'] = user['Idade'] + 35 - (date.today().year - user['Ano de contratação'])
    for k, i in user.items():
        print(f' - {k}: {i}')
else:
    for k, i in user.items():
        print(f' - {k}: {i}')
