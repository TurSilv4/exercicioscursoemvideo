# EU
'''sexo = 'M' or 'F'
while sexo == 'M' and 'F':
    sexo += str(input('Informe o sexo do bebê [M/F] ')).upper()
    print('')
    if sexo != 'M' or 'F':
        print('Valor informado inválido! \n Digite novamente')
print('Acabou')'''

# GUANABARA
sexo = str(input('Por favor. Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Valor inválido! Digite novamente: '))
print('Sexo {} registrado com sucesso.'.format(sexo))
