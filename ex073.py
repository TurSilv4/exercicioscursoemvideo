times = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético Mineiro', 'Ceará', 'Avaí', 'Cuiabá', 'Bragantino', 'Juventude',
         'Flamengo', 'Atlético Goianience', 'Santos', 'Fluminence', 'Palmeiras', 'Fortaleza' ,'Atlético-MG' ,'Botafogo',
         'Internácional', 'Goiás', 'Athletico-PR')
print('=' * 60)
print(times[0:5])
print('=' * 60)
print(times[-4:])
print('=' * 60)
print(sorted(times))
print('=' * 60)
if 'Fluminence' not in times:
    print('A Chapecoence não está na lista!')
else:
    posição = times.index('Fluminence')
    print(f'O Fluminence está na posição {posição+1}')
