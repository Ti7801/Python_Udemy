"""
Funções (def) em Python - *args **kwargs-
"""
"""
def func(a1, a2, a3, a4, a5, nome = None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var =func(1, 2, 3, 4, 5, nome ='Luiz', a6='5')
print (var)

def func(*args):
    print(args)

# O '*n' simboliza o restante da lista
list=[1, 2, 3, 4, 5]
n1, n2, *n = list

print(n1, n2, n)



# O *args é utilizado para corresponder aos argumentos
def func(*args):
    print(args)

# O '*n' simboliza o restante da lista
lista=[1, 2, 3, 4, 5]

# COMO TIRAR OS VALORES DA LISTA E IMPRIMR APENAS ELES-
#DESEMPACOTANDO OS VALORES DA LISTA
# POSSO UTILIZAR UM SEPARADOR SE QUISER
print(*lista, sep='-')



# O *args é utilizado para corresponder aos argumentos
def func(*args):
    print(args)
    print(args[0])
    print(args[-1]) 
    print(len(args))
#ARGUMENTOS EMPACOTADOS EM UMA TUPLA - TUPLA É UMA LISTA QUE NÃO
#SE ALTERA

func(1, 2, 3, 4, 5)



# O *args é utilizado para corresponder aos argumentos
# EU NÃO POSSO ALTERAR OS ELEMENTOS DE UMA TUPLA
def func(*args):
    args[0] = 20
    print(args)

func(1, 2, 3, 4, 5)


# O *args é utilizado para corresponder aos argumentos
# EU NÃO POSSO ALTERAR OS ELEMENTOS DE UMA TUPLA
def func(*args):
    #args = list(args)  # Então a tupla agora virou lista e posso alterar
    #args[0] = 20
    for v in args:
        print(v)

func(1, 2, 3, 4, 5)


# O *args é utilizado para corresponder aos argumentos
# EU NÃO POSSO ALTERAR OS ELEMENTOS DE UMA TUPLA
def func(*args):
    print(args)
    
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)



#Pode ser qualquer coisa esses parâmetros na funcao
# Mas tem que ta dentro da convenção
# nesse exemplo os argumentos nomeados ficam dentro de **kwargs
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])
    
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')




def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)

"""

def func(*args, **kwargs):
    print(args)

    idade = kwargs['idade']
    print(idade)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)










