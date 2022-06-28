"""
Funções (def) em Python - return - (Parte 2 )

def funcao(var):
    return var
    print('Se houver algo após o return, não sera executado')

variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')


# Formas para fazer uma funcao que faz divisão - apenas testando
def divisao(n1, n2):
    #if n2 > 0:
     if n2 == 0:
        return
        #return n1 / n2
     return n1/n2

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta Inválida')




def dumb():
    return 1
    #return True # retorna tipo de dado booleano

var = dumb()

print(var, type(var))


"""



def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('BLAAAAA')

