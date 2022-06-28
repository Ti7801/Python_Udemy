"""
Importância da Documentação - Site de python que salvei no navegador

conversão de string para inteiro

isnumeric, isdigit, isdecimal

Ele levantou a questão de que não podia converter a letra a para um inteiro, caso o usuário digita-se a letra
a em uma das variáveis.....
Então ele estabelece que primeiro você recebe os valores digitados e depois você converte eles em inteiro
dentro de uma condição if, usando funções estabelecidas no python

"""

""""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print('Não pude converter os números para realizar contas!!!')
"""
# TRY E EXCEPT - Tenta executar a parte do try, se houver algum erro execute a parte debaixo!!!!!!!

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
except:
    print('ERROR')








