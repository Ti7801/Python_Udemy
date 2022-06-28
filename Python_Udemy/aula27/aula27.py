"""
* Enumerate - Enumerar elementos da lista
"""


#           0      1      2
lista = [['Edu', 'João', 'Luiz'],  # 0
         ['Maria', 'Aline', 'Joana'],  # 1
         ['Helena', 'Ed', 'Lu'], ]  # 2

# enumerada = list(enumerate(lista))

# print(enumerada[1][1][2])

for v1 in enumerate(lista, 53):
    #print(v1, v2)
    valor_enumerado, minha_lista = v1
    #print(minha_lista)
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2)



