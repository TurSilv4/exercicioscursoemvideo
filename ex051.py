print('=' * 30)
print('{:^30}'.format('''10 TERMOS DE UMA PA'''))
print('=' * 30)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
f = pt + 10 * r
for pa in range(pt, f, r):
    print(pa, end='-> ')
print('ACABOU!')
