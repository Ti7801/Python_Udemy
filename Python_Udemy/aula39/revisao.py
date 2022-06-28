
"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne
o valor da função2 executada

def result(args):
    print(args)

def soma(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    soma = n1 + n2
    return soma

var = soma(9, 4)
result(var)

"""



"""
Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor 
da função2 executada. Faça a função1 executar duas funções que recebam um 
número diferente de argumentos

"""
def funcao1(*args):
    return args

def funcao2(args):
    print(args)

def funcao3(*args, **kwargs):
    args = list(args)
    print(args)
    print(kwargs['nome'], kwargs['Sobrenome'])

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

funcao1(funcao2('FODA-SE'), funcao3(*lista1, *lista2, nome='Tiago', Sobrenome='Miguel'))






