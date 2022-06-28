"""
2 -  Crie uma função que recebe uma função2 como parâmetro e retorne
o valor da função2 executada.Faça a função1 executar duas funções que
recebem um numero diferente de argumentos.

"""

def imprimir(*args):
    print(*args)

def idadeAluno():
    idade = input('Digite a idade da Pessoa: ')
    return idade

def notas(*args):
    nota1 = input(f'Digite a nota 1: ')
    nota2 = input(f'Digite a nota 2: ')
    nota3 = input(f'Digite a nota 3: ')
    return nota1, nota2, nota3

valor = idadeAluno()
#imprimir(valor)
valor1 = notas()
imprimir(valor, *valor1)  # o asterisco foi utilizado para desempacotar
#os valores que apareceram como lista

