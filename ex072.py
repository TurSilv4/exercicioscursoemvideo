extenço = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = int(input('Digite um numero para vê-lo por extenço: [0-20]: '))
while numero > 20:
    numero = int(input('Valor inválido! Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {extenço[numero]}')
