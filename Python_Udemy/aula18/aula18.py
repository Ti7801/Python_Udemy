"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiro (int)
:f - Número de ponto flutuante (float)
:. (NÚMERO)f - QUANTIDADE DE CASAS DECIMAIS ( float)
: (CARACTERE) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

#num_1 = 10
#num_2 = 3
#divisao = num_1 / num_2
#  print('{:.2f}'.format(divisao))
#  print(f'{divisao:.2f}')

#  num_1 = 1
#  print(f'{num_1:0>10}')  # O valor 1 terá 10 casas..... irá ficar 0000000001 - será acrescentado 9 zeros a direita
"""
num_1 = 1150
print(f'{num_1:0>10}')

num_1 = 1150
print(f'{num_1:0<10}')

num_1 = 1150
print(f'{num_1:^010}')

# Adicionar o zero a esquerda e que agora ele tenha 10 casas

num_1 = 1150
print(f'{num_1:0>10.2f}')

nome = 'Tiago Daltro Duarte'
print(f'{nome:#^50}')

nome = 'Tiago Daltro Duarte'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome = 'Tiago Daltro Duarte'
nome_formatado = '{n}{n}{n}'.format(n=nome)
print(nome_formatado)

nome = 'Tiago Daltro Duarte'
nome_formatado = '{n:0<20}'.format(n=nome)  #  QUE REPITA O NOME E SEJA ACRESCENTADO AO FINAL DELA ATE COMPLETAR 20
print(nome_formatado)

nome = 'Tiago'
sobrenome = 'Daltro'
nome_formatado = '{1:#^50}'.format(nome, sobrenome)  #  Passando o indice do sobrenome 1. Que meu sobre nome completo
#tenha exatamente 50 caracteres
print(nome_formatado)

# Existe algumas funções que fazem isso tudo importantes no pyhon

nome = 'Tiago'
nome = nome.ljust(30, '#')
print(nome)


nome = 'Tiago Daltro'
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas











"""

