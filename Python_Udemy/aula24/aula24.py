"""
Listas em Python
fatiamento

append - Inserir valores na lista no final
insert - Inserir valores no começo da lista
pop - Remover o ultimo elemento da lista
del - Deletar um elemento ou uma fatia de elementos da lista
clear - Limpar a nossa lista
extend - Juntar duas listas
min -
max -
range -


# Váriavel so tem um valor
# Uma lista pode conter vários valores de todos os tipos

#texto = 'Valor'
#lista = [1, 2, 3, 4, 'Luiz Otávio', True]

#         0     1    2   3    4
lista = ['A', 'B', 'C', 'D', 'E']
#         -5   -4   -3   -2   -1
# Modificar algum valor que esta em alguma posição dentro da lista
lista[4] = 'Qualquer outra coisa'
#FATIAMENTO
print(lista[0:4:2])  # COMEÇA NO ZERO, VAI ATÉ 4 E PULA DE 2 EM 2
print(lista[4])
print(lista[::-1]) #Ignorando de onde começa, aonde termina e começano de trás pra frente lendo de 1 em 1

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
#print(l3)  # extend - junta duas listas - possui a mesma função do sinal de '+'
l1.extend(l2)
print(l1)
l2.append('b')  # Adicionando 'b' no final da lista l2
print(l2)
l2.insert(0, 'Banana')  # Insere o comentário ou o que você quiser no indice que você informar, no caso ai , indice 0.
print(l2)

l2 = [4, 5, 6]

print(l2)
l2.insert(0, 'banana')
print(l2)

l2.pop()
print(l2)



l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)
del(l2[3:5])
print(l2)

print(max(l2))  # Maior valor da minha lista
print(min(l2))  # Menor valor da minha lista


l2 = range(1, 10)

print(l2)

# O CORRETO SERIA ASSIM

l2 = list(range(0, 100, 8))
l3 = list(range(1, 10))
print(l2)
print(l3)


l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for valor in l4:
    soma = soma + valor
print(soma)


"""

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFzzzz a  "{letra}" NÃO EXISTE NA PALAVRA SECRETA.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal, você ganhou!!!')
        break
    else:
        print(f'A palavra era assim : {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
    print()
































