"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz,
caso contrário, retorne o número enviado.

"""

def palavra(n1):
    n1 = int(n1)
    if n1 % 5 == 0 and n1 % 3 == 0:
        return f'FizzBuzz {n1} é divisivel por 3 e 5'
    if n1 % 3 == 0:
        return f'fizz {n1} é divisivel por 3'
    if n1 % 5 == 0:
        return f'buzz {n1} é divisivel por 5'
    return n1

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(palavra(aleatorio))
