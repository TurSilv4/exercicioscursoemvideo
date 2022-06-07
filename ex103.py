# Faça um programa que tenha uma função chamada ficha() que receba dois parametros: o nome de um jogador e quantos gols ele marcou
# O programa devera ser capaz de mostrar a ficha desse jogador mesmo que algum dado não tenha sido informado corretamente


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) na temporada.')


#Programa principal
user = str(input('Nome do jogador: '))
user_gols = str(input('Gol(s) do campeonato: '))
if user_gols.isnumeric():
    user_gols = user_gols
else:
    user_gols = 0
if user.strip() == '':
    ficha(gols=user_gols)
else:
    ficha(user, user_gols)
