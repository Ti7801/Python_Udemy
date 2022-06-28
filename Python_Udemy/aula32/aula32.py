"""
DESAFIO

FOR/WHILE

usar uma estrutura de repetição e criar dois contadores
esses dois contadores vao ser de uma vez so, o primeiro contador vai ser de maneira progressiva
e o segundo contador vai ser de maneira regressiva.

A cada volta do laço

"""
"""
# Utilizando while
contador1 = -1
contador2 = 11

while contador1 < 8 and contador2 > 2:
    contador1 += 1
    contador2 -= 1
    print(contador1, contador2)

"""
"""
# Utilizando For

contador1 = -1
contador2 = 11


for valor in range(0, 10):
    contador1 = int(contador1)
    contador2 = int(contador2)
    contador1 = contador1 + 1
    contador2 = contador2 - 1

    print(contador1, contador2)

    if contador1 == 8 and contador2 == 2:
        break

"""

# SOLUÇÃO DO PROFESSOR

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)









