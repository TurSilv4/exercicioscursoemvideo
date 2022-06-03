peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.1f} e indica que está:\n "ABAIXO DO PESO"'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f} e indica que está:\n "PESO IDEAL"'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f} e indica que está:\n "SOBREPESO"'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f} e indica que está\n "OBESIDADE"'.format(imc))
else:
    print('Seu IMC é {:.1f} e indica que está\n "OBESIDADE MÓRBIDA'.format(imc))
