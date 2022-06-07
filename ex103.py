# Faça um programa que tenha uma função chamada ficha() que receba dois parametros: o nome de um jogador e quantos gols ele marcou
# O programa devera ser capaz de mostrar a ficha desse jogador mesmo que algum dado não tenha sido informado corretamente


def ficha(nome='<desconhecido>', gols=0):
    n = nome
    gol = gols
    print(f'O jogador {n} fez {gol} gol(s) na temporada.')



#Programa principal
user = input('Nome do jogador: ')
user_gols = input('Gol(s) do campeonato: ')
ficha(user, user_gols)
