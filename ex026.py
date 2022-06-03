frase = str(input('Digite uma frase: ')).upper().strip()
fc = frase.count('A')

print('A letra "A" aparece {} vezes.'.format(fc))

print('Ela aparece na posição {} a primeira vez.'.format(frase.find('A')+1))

print('E, na posiça {} pela ultima vez.'.format(frase.rfind('A')+1))
