# Adpte o codigo do ex107 criando uma funçao adicional chamada moeda()
# Que consiga mostrar os valores como um valor monetário formatado

def dobro(_):
    """
    -> Dobra o valor do parametro passado
    :param _: Recebe um valor
    :return: Retorna o dobro do valor
    """
    return _ * 2


def metade(_):
    """
    -> Divide o valor do parametro passado
    :param _: Rebebe um valor
    :return: Retorna a metade do valor
    """
    return _ / 2


def diminuir(_, p):
    """
    -> Subtrai o percentual indicado
    :param _: Recebe um valor (float, int)
    :param p: Valor percentual a ser descontado
    :return: Retorna o valor com desconto
    """
    return _ - (_ * p / 100)


def aumentar(_, p):
    """
    -> Adiciona o percentual indicado
    :param _: Recebe um valor (float, int)
    :param p: Valor a ser adicionado
    :return: Retorna o valor com o juros
    """
    return _ + (_ * p / 100)


def moeda(_):
    return f'R${_:.2f}'
