# Modifique as funçoes qeu foram criadas no ex107 para que elas aceitem um parametros a mais informando
# Se o valor retornado por elas vai ser ou não formatado pela função moeda do ex108

def moeda(_):
    return f'R${_:.2f}'


def dobro(_, f):
    """
    -> Dobra o valor do parametro passado
    :param _: Recebe um valor
    :param f: Opcional se True mostra o valor formatado senão Apenas retorna o valor
    :return: Retorna o dobro do valor
    """
    if f:
        r = _ * 2
        return moeda(r)
    else:
        return _ * 2


def metade(_, f):
    """
    -> Divide o valor do parametro passado
    :param f: Parametro opcinal (Se True mostra o valor formatado senão apenas retorna o valor
    :param _: Rebebe um valor
    :return: Retorna a metade do valor
    """
    if f:
        r = _ / 2
        return moeda(r)
    else:
        return _ / 2


def diminuir(_, p, f):
    """
    -> Subtrai o percentual indicado
    :param _: Recebe um valor (float, int)
    :param p: Valor percentual a ser descontado
    :param f: Opcional (se True retorna o valor formatado senão apenas retorna o valor
    :return: Retorna o valor com desconto
    """
    if f:
        r = _ - (_ * p / 100)
        return moeda(r)
    else:
        return _ - (_ * p / 100)


def aumentar(_, p, f):
    """
    -> Adiciona o percentual indicado
    :param _: Recebe um valor (float, int)
    :param p: Valor a ser adicionado
    :param f: Opcional (se True retorna o valor formatado senão apenas retorna o valor
    :return: Retorna o valor com o juros
    """
    if f:
        r = _ + (_ * p / 100)
        return moeda(r)
    else:
        return _ + (_ * p / 100)
