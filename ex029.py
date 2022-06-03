v = float(input('Qual a velocidade do carro?: '))

multa = (v - 80) * 7

if v > 80:
    print('Você excedeu o limite de 80Km/H \n e recebeu uma multa no valor de R${:.2f}.'.format(multa))

else:
    print('Tenha um bom dia! Dirija com segurança')