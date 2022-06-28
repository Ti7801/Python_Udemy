"""
While

utilizado para realizar ações enquanto uma condição for verdadeira.
Requisitos : Entender condições e operadores
"""
"""
while True:  # loop infinito
    nome = input('Qual o seu nome? ')
    print(f'Olá {nome}')
print('Não sera executada nunca')


#  Um contador  de 1 até 100
x = 0
while x < 5:
    print(x)
    x = x+1
print('Acabou')


# Continue é usada para pular para o proximo laço
x = 0
while x < 10:
    if x == 3:
        #  x = x + 1  # PARA RESOLVER FAZ ISSO AQUI (SEM ISSO ENTRA EM UM LOOP INFINITO)
        print(x)
        continue
    print(x)
    x = x + 1

#  Utilizando o break, finaliza o loop!!!
x = 0
while x < 10:
    if x == 3:
          x = x + 1
          break

    print(x)
    x = x + 1



x = 0  # coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y = y + 1
    print(x)
    x += 1  # x = x + 1
print('Acabou!!!')

"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric or not num_2.isnumeric:
        print('Você precisa digitar um número')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
         print(num_1 + num_2)

    elif operador == ' - ':
        print(num_1 - num_2)

    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')












