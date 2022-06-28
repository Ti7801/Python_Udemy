"""
Desempacotamento de listas e Python

"""

lista = ['Luiz', 'João', 'Maria', 2, 3, 4, 5, 6, 7, 9, 100]
#n1, n2, n3 = lista
# n1, n2, *outra_lista, ultimo_da_lista = lista  (aqui ele pega os dois primeiros valores e cria outra lista com
*outra_lista, n1, n2, n3 = lista                  #  o resto dos valores)
print(n1)

