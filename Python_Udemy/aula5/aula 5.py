"""
+, -, /, //,
** -- Exponenciação
%,
()
"""

print(10 * 10)  # Multiplicação - O operador de multiplicação tbm serve como operador de repetição
print(10 + 10)  # Adição
print(10 - 5)   # Subtração
print(10 / 2)   # Divisão

print(10 ** 2)  # Elevado a 2 (potênciação)

print('5' + '5')  # Estarei juntando os dois numeros, ficará 55. Não ficará 10 porque são duas strings.

print('Luiz'+' '+ 'Otávio') # CONCATENA OS STRINGS..

print('Luiz'+ ' '+'Otávio e ele tem ' + str(32) + 'anos')  # Concatena os strings e transforma o inteiro em string.

print(10.5//3)  # Divisão inteira - Vai retornar apenas a parte inteira.

print(10.5/3)  # Retornar o valo da divisão normalmente.

print(10%5)  # Divisão com resto da divisão

print(5+2*10) # Siga as regras igual na matemática (2 vezes 10, e depois some a 5)

print((5+2)*10)  # Separando as operações com parênteses


#Precedência dos Operadores Aritméticos


# (n+n) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro
# ** - Depois vem a exponenciação
# * /  //  % - Na sequência multiplicação, divisão, divisão inteira e módulo(divisão com resto)
# + - (Por fim, soma e subtração)



#  2 + 5 * 3 ** 2 - (23.5 + 23.5) = 47 - 47 = 0

