"""
1 - CRIE UMA FUNÇÃO QUE EXIBE UMA SAUDAÇÃO COM OS PARÂMETROS SAUDAÇÃO E NOME

def funcao(suadacao, nome):
    print(suadacao, nome)

funcao("Bom dia", "Gabriel")
"""

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles

def funcao(n1, n2, n3):
    soma = n1+n2+n3
    return soma

var = funcao(4, 5, 7)

print(var)

"""

"""
3 - Crie uma função que recebe 2 números. O primeiro é um valor e o segundo 
um percentual(ex.100%). Retorne(return) o valor do primeiro número somado do 
aumento do percentual do mesmo.


def valor(x, percentual):
    percentual = percentual/100
    aumento = (x * percentual)
    resultado = x - aumento
    return resultado

var = valor(20, 50)

print(var)
"""


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro 
da função for divisível por 5  e por 3, retorne fizzBuzz, caso contrário, retorne
o número enviado.

def divisao(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'fizzBuzz'
    if n1 % 5 == 0:
        return 'buzz'
    if n1 % 3 == 0:
        return 'fizz'

    return n1

print(divisao(15))



"""