"""
Funções Parte 4

#  ESCOPO GLOBAL, OU SEJA ESTÁ ACESSIVEL EM TODO O CODIGO

variavel = 'valor'

def func():
    print(variavel)


def func2(arg=None):
    # PARA ALTERAR VARIAVEIS GLOBAIS DENTRO DE UMA FUNÇÃO
    # NÃO É UMA BOA PRATICA DE PROGRAMAÇÃO
    #global variavel
    #variavel = 'Outro Valor'  # criada dentro do escopo local da função
    #print(variavel)
    # Replace substitui um string por outro
    arg = arg.replace('v', 'c')
    return arg

func()
#func2()
outra_variavel = func2(arg=variavel)


print(variavel)
print(outra_variavel)



"""


variavel = 'valor'

# tudo que ficar fora da funcao está no escopo global
# Posso acessar dentro da função mas não posso alterar sem usar
# a palavra global como foi falado no exemplo em cima.
def func():
    # aqui dentro da erro pq ele não ta considerando a variavel global
    # ta considerando a variavel local dentro da funcao
    #print(variavel)
    #variavel = 1234
    #print(variavel)
    outra_variavel = 'valor'
    return outra_variavel

def func2(args):
    print(args)

var = func()
func2(var)
