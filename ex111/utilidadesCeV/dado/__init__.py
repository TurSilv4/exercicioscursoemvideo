def leiadinheiro(_):
    while True:
        try:
            valido = False
            while not valido:
                entrada = str(input(_)).replace(',', '.').strip().replace(' ', '')
                if entrada.isalpha() or entrada == '':
                    print(f'\033[0;31m"{entrada}" é um valor inválido\033[m')
                else:
                    valido = True
                    return float(entrada)
            break
        except:
            print(f'\033[0;31mERRO! Não insira letras ao valor\033[m')