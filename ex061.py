print('=' * 30)
print('{:^30}'.format('''10 TERMOS DE UMA PA'''))
print('=' * 30)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
