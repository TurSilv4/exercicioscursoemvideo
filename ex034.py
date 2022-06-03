s = float(input('{}Digite o salário R$:{}'.format('\033[30m', '\033[m')))

                                            #MEU FORMATO
'''au = s + (s * 0.1)
au2 = s + (s * 0.15)

if s > 1250:
    print('Salários de R${:.2f} \n Recebem aumento de 10% \n Passabdo a ser R${:.2f}'.format(s, au))

else:
    print('salários de {:.2f} \n Recebem aumento de 15% \n Passando a ser {:.2f}'.format(s, au2))'''

                                        #FORMATO DO GUANABARA
if s <= 1250:
    aumento = s + (s * 15 / 100)

else:
    aumento = s + (s * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(s, aumento))
