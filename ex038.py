n1 = int(input('\033[34mPrimeiro valor: \033[m'))
n2 = int(input('\033[36mSegundo valor: \033[m'))
print('')

if n1 > n2:
    print('\033[34mO PRIMEIRO valor "{}" é o maior.\033[m'.format(n1))

elif n2 > n1:
    print('\033[36mO SEGUNDO valor "{}" é o maior.\033[m'.format(n2))

else:
    print('\033[37mOs dois valores são IGUAIS.\033[m')
