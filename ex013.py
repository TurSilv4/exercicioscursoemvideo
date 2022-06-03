s = float(input('Salário:'))
#a = s * 0.15
#r = s + a
#print('Salário atual R${:.2f} \nome Valor do aumento R${:.2f} \nome Novo salário R${:.2f}'.format(s, a, r))
a = s + (s * 15/100)
print('O aumento de salario vai para R${:.2f}'.format(a))
