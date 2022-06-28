"""
Funções Anônimas = LAMBDAS

Muito importante  quando você precisa passar uma função como
parâmetro para outra função



def funcao(arg, arg2):
    return arg* arg2

var = funcao(2,2)

# não tem parênteses, não tem as chaves e nem return
# Anonima porque não possui nome

a =lambda x, y: x * y

print(a(2, 2))



lista = [
    ['P1', '13'],
    ['P2', '6'],
    ['P3', '7'],
    ['P4', '50'],
    ['P5', '8'],
]
# Ordenando as listas

def func(item):
    return item[1]

#lista.sort(key=func)
#print(lista)

#lista.sort(key=func, reverse=True)
#print(lista)

" ou  "

lista.sort(key=lambda item: item[1])

print(lista)


lista = [
    ['P1', '13'],
    ['P2', '6'],
    ['P3', '7'],
    ['P4', '50'],
    ['P5', '8'],
]

print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista)


"""

