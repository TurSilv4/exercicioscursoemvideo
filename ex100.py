#Faça um programa que tenha uma lista chamada numeros e duas funçoes chamadas sorteio() e somapar().
#A primeira funçao vai sortear 5 numeros e colocar dentro de uma lista e a;
#Segunda vai mostrar a soma entre todos os numeros pares sorteados pela função anterior

from random import randint
from time import sleep

numeros = list()
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 20)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def SomaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores Pares de {lista} temos {soma}')



sorteia(numeros)
sleep(0.5)
SomaPar(numeros)

