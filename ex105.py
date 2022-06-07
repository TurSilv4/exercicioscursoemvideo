# Faça um programa que tenha uma função notas() que pode receber varias notas e vai retornar um dicionario com as informações:
# quantidade de notas; a maior nota; a menor nota; a media da turma; a situaçao (opcional) adicione tambem as doc strigs

def notas(*n, sit=False):
    """
    -> Funçao para analizar notas e situações de vários alunos
    :param n: Recebe vários valores
    :param sit: (Opcional) Mostra a situação geral da sala
    :return: Retorna o dicionario mostrando a situação da nota
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['sit'] = 'Boa'
        elif 7 > r['media'] >= 5:
            r['media'] = 'Regular'
        else:
            r['media'] = 'Ruim'
    return r


# Programa prncipal


resp = notas(5.5, 2.5, 1.5, sit=True)  #sit é um parametro opcional
print(resp)
