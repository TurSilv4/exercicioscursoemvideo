# EU

'''numero = quantia_numero = divisao = maior = menor = 0
continuar = 'S'
while continuar != 'N':
    numero = int(input('Digite um valor: '))
    quantia_numero += 1
    divisao += numero
    continuar = str(input('Deseja continuar [S/N] ')).upper()
    print('')
    if numero > maior:
        maior = numero
    elif menor < maior:
        menor = numero
print('Foram informados {} numeros'.format(quantia_numero))
print('Sua média é a de {:.1f} '.format(divisao / quantia_numero))
print('Sendo {} o MAIOR e {} o MENOR'.format(maior, menor))'''

# GUANABARA

resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / quant

print('Você digitou {} numero e a media deles é {:.2f}'.format(quant, media))
print('O MAIOR valor foi {} e o MENOR foi {}'.format(maior, menor))
