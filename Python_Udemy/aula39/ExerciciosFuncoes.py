"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne
o valor da função2 executada
"""


def soma(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    soma = n1+n2
    return soma

def imprimir(*args):
    print(*args)

resultado = soma(10,5)

imprimir(resultado)



