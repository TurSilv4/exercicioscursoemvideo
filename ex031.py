d = float(input('Qual a distância da viagem: '))

p = d * 0.5 if d <= 200 else d * 0.45               #SIMPLIFICADO

'''if d <= 200:
    p = d * 0.5

else:
    p = d * 0.45'''                                 #COMPOSTO

print('O valor da Viagem será de R${:.2f}.'.format(p))
