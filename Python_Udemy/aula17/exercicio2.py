"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudações apropriada.
Exemplo: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""


hora = input('Digite a hora atual considerando os numeros de 0 a 23: ')

if hora.isdigit():
    hora = int(hora)
    if (hora > 0) and (hora <= 11):
        print('Bom dia ')
    elif (hora >= 12) and (hora <= 17):
        print('Boa tarde')
    elif (hora >= 18) and (hora <= 23):
        print('Boa noite')
else:
    print('Digite um numero inteiro estabelecido entre o intervalo!!!!!!')


