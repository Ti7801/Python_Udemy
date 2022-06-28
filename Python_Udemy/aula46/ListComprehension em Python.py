"""
Compreensões de Listas

Motivos: Otimização e escrever menos linhas( serve para isso)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Pegando os valores de l1 e jogando dentro da variavel e criando uma nova
#lista
l2 = [variavel for variavel in l1]
print(l2)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)

l2 = ['Luiz', 'Mauro', 'Maria']

ex4 = [v.replace('a', '@') for v in l2]

print(ex4)



tupla = (('chave', 'valor'),
         ('chave2', 'valor2'),
)

ex5 = [(x, y) for x, y in tupla]
ex5 = dict(ex5)

#print(ex5)
#print(ex5['chave2'])


# Lista de todos os números divisiveis por 2 .
l3 = list(range(100))

# print(l3)

ex6 = [v for v in l3 if v % 2 == 0]

print(ex6)




# Lista de todos os números divisiveis por 3 e por 8 .
l3 = list(range(100))

# print(l3)

ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

print(ex6)


# Lista de todos os números divisiveis por 3 se não for coloque zero no local do numero.
l3 = list(range(100))


ex7 = [v if v % 3 == 0 else 0 for v in l3]

print(ex7)



# Lista de todos os números divisiveis por 3  e por 8, caso não seja, coloque zero no local do numero.
l3 = list(range(100))


ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(ex7)
"""

