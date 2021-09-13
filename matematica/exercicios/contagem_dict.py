def contar_caracteres(s):
    """"
    func q conta os caracteres da lista
    Ex:
    >>> contar_caracteres('tartiner')
            {'a':1, 'e':1, 'i':1, 'n':1, 'r':2, 't'':2}

    :param s:lista
    :return
    """
    resultado= {}
    for caracter in s:
        resultado[caracter]= resultado.get(caracter, 0) +1

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('martin'))
    print()
    print(contar_caracteres('banana'))

