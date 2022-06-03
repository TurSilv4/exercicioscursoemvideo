# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses:
# Seu programa deverá analizar se a expressão está com os parenteses abertos e fechados na ordem correta

expressao = str(input('Informe a espressão: '))
total_parenteses = []
for caractere in expressao:
    if caractere == '(':
        total_parenteses.append('(')
    elif caractere == ')':
        if len(total_parenteses) > 0:
            total_parenteses.pop()
        else:
            total_parenteses.append(')')
            break
print('A sua expressão está correta' if len(total_parenteses) == 0 else'A sua espressão está incorreta')
