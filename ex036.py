casa = float(input('Qual o valor da casa que pretende comprar: R$'))
salario = float(input('Salário que recebe por mês: R$'))
parcela = int(input('E em quantos anos: '))
valor = casa / parcela / 12

if valor <= salario * 0.3:
    print('PARABENS! Seu emprestimo foi \033[32mAPROVADO\033[m.\n '
          'O valor da prestação mensal é a de R${:.2f}'.format(valor))
else:
    print('Infelizmente o seu empréstimo foi \033[31mNEGADO\033[m!')

'''casa = float(input('Valor da casa R$'))
salario = float(input('Salário do comprador R$'))
anos = int(input('Quantos anos de financiamento: '))
parcela = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos\n'
      ' A prestação sera de R${:.2f}'.format(casa, anos, parcela))
if parcela <= minimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
    '''