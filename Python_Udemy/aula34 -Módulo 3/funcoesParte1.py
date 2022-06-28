"""
Funções - def em Python (Parte 1 )

"""
"""
def funcao(msg):
    print(msg)

funcao('Eu posso escrever o que eu quiser aqui')

def saudacao(msg,nome):
    print(msg, nome)

saudacao('Olá','Luiz Otávio')

def saudacao(msg = 'Olá', nome = 'Usuário'):
    print(msg, nome)

saudacao(nome= 'Zezinho', msg= 'Hi')

def saudacao(msg = 'Olá',nome = 'usuário'):
    nome = nome.replace('e', '3')  #  Aonde tem 'e' ele bota 3
    msg = msg.replace('e', '3')
    print(msg, nome)

saudacao(nome='zezinho', msg= 'Hi')


def saudacao(msg = 'Olá',nome = 'usuário'):
    nome = nome.replace('e', '3')  #  Aonde tem 'e' ele bota 3
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)




"""

