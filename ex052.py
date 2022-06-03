num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n \033[34mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('\033[32mE por isso ele É um número PRIMO')
else:
    print('\033[31mE por isso ele NÂO é um número PRIMO')
