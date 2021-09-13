def contar_caracteres(s):
    """"
    func q conta os caracteres da lista
    Ex:
    >>> contar_caracteres('Tartine'):
            a=1
            e=1
            i=1
            n=1
            r=1
            t=2




    :param s:lista
    :return
    """
    caractere_ordenados= sorted(s)

    caractere_anterior= caractere_ordenados[0]
    contagem=1

    for caracter in caractere_ordenados[1:]:
        if caracter == caractere_anterior:
            contagem+=1
        else:
            print(f'{caractere_anterior}={contagem}')
            caractere_anterior=caracter
            contagem = 1
    print(f'{caractere_anterior}={contagem}')

if __name__ == '__main__':
    contar_caracteres('martin')
    print()
    contar_caracteres('tartiner')

