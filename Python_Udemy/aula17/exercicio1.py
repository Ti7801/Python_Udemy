"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

num1 = input('Informe um número inteiro: ')

if num1.isdigit():
    num1 = int(num1)
    if num1 % 2 == 0:
        print('Este número é PAR!!!!')
    else:
        print('Este número é impar')
else:
    print('O número não é inteiro')
