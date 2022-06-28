"""
Split, Join, Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""


#string = string.split('')  #  Usando a string pra virar lista. E as palavras vão estar separadas por espaço.
#print(string)

"""
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')

*********************************************************************

string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:  # capitalize() - deixar a primeira letra da frase maiusculo
    print(valor.strip().capitalize())  # removendo o espaço com strip() do inicio e do fim da string.



***********************************************************************


string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string)
print(lista)
print(string2)

string = 'O Brasil é penta.'
lista = string.split(' ')

# v1 como indice e v2 como valor - desempacotando o elemento

for v1, v2 in enumerate(lista):
    print(v1, v2, lista[v1])


# Uma lista pode conter outras listas

lista = [[0, 'Luiz'], [1, 'João'], [2, 'Maria'], ]


for indice, nome in enumerate(lista):
    print(indice, nome)





"""





