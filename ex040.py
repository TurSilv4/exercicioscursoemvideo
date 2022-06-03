n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('\033[31mSua média é {:.1f}\n Você foi REPROVADO\033[m'.format(media))

elif 5.0 <= media <= 6.9:
    print('\033[33mSua média é {:.1f}\n Você está de RECUPERAÇÃO\033[m.'.format(media))

elif 7.0 <= media:
    print('\033[32mPARABENS!\n Sua média é {:.1f}\n Você foi aprovado.\033[m'.format(media))
