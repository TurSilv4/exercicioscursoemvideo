from datetime import date
data = date.today().year
maior = 0
menor = 0
for n in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(n)))
    d = data - nasc
    if d >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são MAIORES de idade'.format(maior))
print('{} pessoas são MENORES de idade'.format(menor))
