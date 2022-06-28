"""
Introdução a formatação de  strings
"""

nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade >18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))  # Colocando as variáveis em ordem.
print('{im} {n} tem {i} anos de idade e seu imc é '.format(n=nome, i=idade, im=imc))








