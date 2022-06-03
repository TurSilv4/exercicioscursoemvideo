def soma(a, b): #2 parametros / Só recebe esses dois valores
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4) #Da erro pq foi passado no def 2 parametros (a, b) ent tem que ser o valor determinado

soma(b=4, a=5) #Posso declarar as variaveis dos valores / Podendo trocar a ordem dos valores
soma(7, 2) # Se não explicitado o valor de A sempre é o primeiro e B o segundo valor

#DESEMPACOTAR PARAMETROS
    #Tuplas
def contador(*num): #Cria parametros variaveis / Recebe varios valores
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

contador(2, 1, 7)           #\
contador(8, 0)              # > Cria uma tupla com os valores de num
contador(4, 4, 7, 6, 2)     #/

    #Listas
valores = [6, 3, 9, 1, 0, 2]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
dobra(valores) # Oq acontecer na lista Valores interfere em (lst)
print(valores)
