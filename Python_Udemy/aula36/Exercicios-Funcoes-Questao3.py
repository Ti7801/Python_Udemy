"""
3 - crie uma função que receba 2 numeros. O primeiro é o valor e o
segundo um percentual (exemplo: 10%). Retorne(return) o valor do
primeiro número somado do aumento do percentual do mesmo.

"""
def numeros(n, porcentagem):
    porcentagem = float(porcentagem/100)
    n = int(n)
    resultado = float(n * porcentagem)
    return n + resultado

a = numeros(5, 50)

print(a)
