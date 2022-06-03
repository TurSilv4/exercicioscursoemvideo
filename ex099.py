#Faça um programa que tenha uma função chamada maior(). que receba vários parametros com valore s inteiros.
#Seu programa tem que anallizar todos os valores e dizer qual deles é o maior
from random import randint
from time import sleep


def maior(*num):
    print('=' * 40)
    print('Analizando os valores passados...')
    for c in num:
        print(c, end=' ')
        sleep(0.4)
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)if len(num) != 0 else 0 } ')


maior(2, 9, 4, 5, 7, 1)
sleep(0.5)
maior(4, 7, 0)
sleep(0.5)
maior(1, 2)
sleep(0.5)
maior(6)
sleep(0.5)
maior()
print('FIM...')
