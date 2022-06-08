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


def resumo(_, n1, n2):
    """
    -> Mostra um resumo de informações
    :param _: Valor relatado
    :param n1: Valor percentual que vai ser acrecentado
    :param n2: Valor percentural que vai ser reduzido
    :return: none
    """
    aumento = _ + (_ * n1 / 100)
    redução = _ - (_ * n2 / 100)

    print('-' * 31)
    print(f'{"RESUMO DO VALOR":^31}')
    print('-' * 31)
    print(f'{"Preço analizado:":<20}{moeda(_)}')
    print(f'{"Dobro do preço:":<20}{dobro(_, True)}')
    print(f'{"Metade do preço:":<20}{metade(_, True)}')
    print(f'{n1}{"% de aumento:":<18}{moeda(aumento)}')
    print(f'{n2}{"% de redução:":<18}{moeda(redução)}')
