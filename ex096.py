#Faça um programa que tenha uma função chamda area(), que receba as dimensoes de um terreno retangular
#(largura e compriento) e mostre a area do terreno


a = float(input('Largura: '))
b = float(input('Comprimento: '))


def area():
    print(f'A área de um terreno {a} x {b} é {a * b:.1f}m²')


area()
