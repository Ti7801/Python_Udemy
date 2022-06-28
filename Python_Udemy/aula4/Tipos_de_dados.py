"""
Tipos de Dados

str - string
int - inteiro
float - real/ponto flutuante
bool - booleano/lógico - True/False Ex: 10==10
"""

print(  type('Luiz')   ) # chamando uma função, uma classe type

print('Luiz', type('Luiz'))
print(10,type(10))
print(25.23,type(25.23))
print(10==10, type(10==10))
print('L'=='L', type('L'=='L'))
print(0.0,type(0))
print(bool(''))  # VALOR BOOLEANO


# FAZENDO CAST
# CONVERTENDO UM TIPO PARA OUTRO TIPO DE DADOS (Conversao de tipo)

print('Luiz',type('Luiz'), bool('Luiz'))
print('10',type('10'), type(int('10')))
print('Luiz', float('10.5'))

# Exercício

#String: nome
print('Tiago',type('Tiago'))
#Idade: int
print(26, type(26))
#Altura: float
print(1.70, type(1.70))
#É maior de idade
print(26>18,type(26>18))

























