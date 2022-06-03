#Fazer programa que tenha um função cantador() que rceba 3 parametros: inicio, fim e passo e realize a contagem
#A) de 1 até 10
#B) de 10 ate 0 de 2 em 2
#C) uma contagem personalizada
from time import sleep


def contador(a, b, c):
    print(f'De {a} até {b} de {c} em {c}:')
    for c in range(a, b+1 if b > 0 else b-1, c):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


def linha():
    print('=-' * 15)


contador(1, 10 ,1)
linha()
contador(10, 0, -2)
linha()
print('Agora é sua vez de personalizar a contagem!')
contador(a=int(input('Início: ')),
         b=int(input('Fim: ')),
         c=int(input('Passo: ')))
