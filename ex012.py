p1 = float(input('Preço: R$'))
#vd = p1 * 0.05
#d = p1 - vd
#print('O valor do desconto é de: R${:.2f} \nome Novo Preço R${:.2f}'.format(vd, d))

d = p1 - (p1 * 5 / 100)
print('O produto vai custar :R${:.2f}'.format(d))
