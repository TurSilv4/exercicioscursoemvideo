#Cria um programa que tenha uma função() chamada voto() que vai receber como parametro o ano de nascimento
# de uma pessoa, retorando o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, oU OBRIGATORIO
from datetime import date


def voto(idade):
    if idade < 16:
        return 'Não vota'
    elif 16 <= idade < 18 or idade >= 65:
        return 'Voto opcional'
    else:
        return 'Voto obrigatório'


# Programa principal
user = int(input('Ano de nascimento: '))
idade = date.today().year - user
voto = voto(idade)
print(f'Com {idade} anos: {voto}')
