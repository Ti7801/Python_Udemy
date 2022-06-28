
from random import randint
numero = str(randint(100000000, 999999999))

lista1 = []
lista2 = []
lista_total = []
lista3 = []
lista4 = []
lista_total1 = []
cpf_novo = []

i = 0
soma = 0
i1 = 0
soma1 = 0

for v in numero:
    v = int(v)
    cpf_novo.append(v)

#  cpf = input('Digite o número do seu cpf: ')

for valor1 in cpf_novo[0:9]:
    valor1 = int(valor1)
    lista1.append(valor1)
#print(lista1)

for valor2 in range(10, 1, -1):
    valor2 = int(valor2)
    lista2.append(valor2)
#print(lista2)

while i < len(lista1):
    lista_total = lista1[i] * lista2[i]
    soma = soma + lista_total
    #print(f'{lista1[i]} * {lista2[i]} = {lista_total}')
    i = i + 1

#print(f' A soma é: {soma}')
#print('\n')

resultado1 = 11 - (soma % 11)

if resultado1 > 9:
    res = 0
    lista1.append(res)
elif resultado1 < 9:
    lista1.append(resultado1)

#print(lista1)

#print(f'AQUI COMEÇA A SEGUNDA INTERAÇÃO DO CODIGO!!')

#print('\n')
# FAZENDO A SEGUNDA PARTE DO PROGRAMA

for valor3 in lista1[0:10]:  # conte de 0 até o último elemento da lista 1
    valor3 = int(valor3)
    lista3.append(valor3)
#print(lista3)

for valor4 in range(11, 1, -1):
    valor4 = int(valor4)
    lista4.append(valor4)
#print(lista4)

while i1 < len(lista3):
    lista_total1 = lista3[i1] * lista4[i1]
    soma1 = soma1 + lista_total1
    #print(f'{lista3[i1]} * {lista4[i1]} = {lista_total1}')
    i1 = i1 + 1
#print(f'A soma é: {soma1}')

resultado2 = 11 - (soma1 % 11)

if resultado2 > 9:
    valor5 = 0
    lista3.append(valor5)
elif resultado2 <= 9:
    lista3.append(resultado2)


stringCpf = []
for digito in lista3:
    stringCpf.append(str(digito))

print(f'{"".join(stringCpf[0:3])}.{"".join(stringCpf[3:6])}.{"".join(stringCpf[6:9])}-{"".join(stringCpf[9:11])}')

