# EU
'''numero = soma = quantos_numeros = 0
while numero != 999:
    numero = int(input('Digite um valor [999 para parar]: '))
    if numero != 999:
        soma += numero
        quantos_numeros += 1
print('Foram digitados {} numeros e a soma deles é {}'.format(quantos_numeros, soma))
'''
# GUANABARA
numero = soma = cont = 0
numero = int(input('Digite um valor: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um valor: '))
print('Foram informados {} numeros e a soma entre eles é {}'.format(cont, soma))
