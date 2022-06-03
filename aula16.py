lanche = ('Hamburguer', 'suco', 'pizza', 'pudim', 'almondegas', 'arroz', 'feijão')
#tuplas são imutáveis
# não funciona____ lanche[1] = 'guarana'
print(lanche[0::2])
for comida in lanche:
    print(f'Eu vou comer {comida}')
# CLÁSSICO SEM A NECESSIDADE DE MOSTRAR A POSIÇÃO

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# MELHOR QUANDO É NESCESSARIO DE MOSTRAR A POSIÇÃO DO ELEMENTO

for posição, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posição}')
# MAS TAMBEM É POSSIVEL ENUMERAR A POSIÇÃO
print('Comi pacas.')

print(sorted(lanche))
# ORGANIZA EM ORDEM ALFABETICA

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# JUNTA TODOS OS ELEMENTOS DA TUPLA (SEM MISTURAR) ALTERAR A ORDEM DO A + B OU B + A ALTERA TAMBEM O RESULTADO
print(c)

print(c.count(3))
# CONTA QUNATES VEZES APARECE O VALOR INDICADO
print(c.index(4))
# MOSTRA EM QUE POSIÇÃO ESTÁ O VALOR INDICADO

pessoa = ('Arthur', 21, 'M', 60.00,)
print(pessoa)
# EM TUPLAS PODE HAVER VÁRIOS TIPOS PRIMITIVOS DIFERENTES (STR, INT, FLOAT, BOOL)

del pessoa
print(pessoa) # DÁ ERRO
# É POSSIVEL DELETAR A TUPLA, MAS, APENAS INTEIRA E NÃO UM SÓ INTEM