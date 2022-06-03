palavras = ('Escola', 'historia', 'computador', 'aventureiro', 'travesseiro', 'mesa', 'celular', 'portao',
            'geladeira', 'gato')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogáis: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

