"""
while/else
contadores
acumuladores
"""

contador = 1
acumulador = 1


while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1

else:  # Esse Else so será executado quando o laço do while for falso, ou seja contador > 10
    print('Cheguei no else.')
print('Isso será executado')  # Essa linha é executada normalmente mesmo a condição do while não sendo falsa.

