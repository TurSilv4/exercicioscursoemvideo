#Cria um programa que tenha uma função() chamada voto() que vai receber como parametro o ano de nascimento
# de uma pessoa, retorando o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, oU OBRIGATORIO

def voto(idade):
    from datetime import date
    idade = date.today().year - user

    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatório'


# Programa principal
user = int(input('Ano de nascimento: '))
print(voto(user))
