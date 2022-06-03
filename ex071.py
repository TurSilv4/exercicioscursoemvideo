from time import sleep
print('=' * 41)
print('{:^41}'.format('''Arthur's Bank Corporation'''))
print('=' * 41)
print('Caixa Eletronico n°000867')
print('-' * 26)
print('{:^21}'.format('''SAQUE'''))
print('-' * 21)
print('''Cédulas disponíveis:
  R$50,00  R$10,00
  R$20,00  R$1,00''')
print('-' * 21)

saque = int(input('Qual o valor a ser sacado: R$'))
print('-' * 21)
print('{:^21}'.format('Insira o cartão'))
print('-' * 21)
sleep(2)
print('{:^21}'.format('Retire o cartão'))
sleep(1.5)
print('=' * 21)
print('{:^21}'.format('Contando cédulas'))
print('=' * 21)
print('')
sleep(3)
total = saque
cedulas = 50
total_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedulas:.2f}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
print('=' * 39 )
print('{:^39}'.format('''Arthur's Bank'''))
print('{:^39}'.format('AGRADECE A SUA PREFERÊNCIA.'))
print('{:^39}'.format('VOLTE SEMPRE!'))