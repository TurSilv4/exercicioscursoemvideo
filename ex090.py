# Fazer um que leia nome e media de um aluno guardados tambem a situção em um dicionario e mostre no final

aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
elif aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
print('=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
