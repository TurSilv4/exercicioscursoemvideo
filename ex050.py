'''s = 0
for c in range(1, 6+1):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
print('A soma dos numeros pares sâo {}'.format(s))
'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print('Voce informou {} números PARES e a sua soma é {}'.format(cont, soma) )