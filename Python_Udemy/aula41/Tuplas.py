"""
Tuplas em Python

Nas tuplas você não pode editar nem adicionar os elementos

utiliza parênteses

"""
"""
t1 = (1, 2, 3, 'a', 'Luiz Otávio')

print(t1)
print(t1[4])

for v in t1:
    print(v)

print(t1[2:])

# Se eu não adiciono a virgula, eu não crio a tupla
t1 = 1, 2, 'a', 'b'
print(t1)

# se colocar assim isso é so um inteiro
t1 = 1

# Agora é uma tupla
#CONCATENANDO AS TUPLAS
t1 = 1, 2, 'Luiz', 4, 5
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

print(t3)

n1, n2, n3, *_, n10 = t3
print(n10)


# REPETIR A TUPLA 20 VEZES NA TELA

t1 = (1, 2, 'Luiz', 4, 5) * 20
print(t1)

# CONVERTENDO TUPLAS EM LISTAS


t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)


"""




