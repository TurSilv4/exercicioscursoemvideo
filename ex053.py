'''frase = str(input('Digite uma frase: ')).replace(' ', '')
contra = frase[::-1]
print('O inverso de {} é {}'.format(frase, contra))
if frase == contra:
    print('\033[32mSendo assim ela É um palíndromo.')
else:
    print('\033[31mSendo assim ela NÃO é um palíndromo'.format(frase))'''

'''frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Sua frase ao contrario é {}'.format(inverso))
if junto == inverso:
    print('Portanto ela É um palíndromo')
else:
    print('Portanto ela NÃO é um palíndromo')'''


