"""
Dicionarios é uma estrutura de dados que suporta um par de chaves
e valor

Nas listas o python gera um indice pra vocÊ 0,1,2,3....

No dicionário você controla o Indice



ObSERVAÇÃO :  LISTAS - COLCHETES
              TUPLAS - PARÊNTESES
              DICIONÁRIO - CHAVES


d1 = {'chave1': 'valor de chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1'])
print(d1['nova_chave'])

CONSTRUTOR

dict - CRIA UM DICIONARIO

d2 = di ct(chave1='valor da chave', chave2='Valor da outra chave')
print(d2['chave1'])
print(d2['chave2'])



d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla',
}
print(d1[(1,2,3,4)])

d1['naoexiste'] = 'Agora existe.'

if 'naoexiste' in d1:
    # Tentar acessar chave que não existe.
    print(d1['naoexiste'])

print('OI')



d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla',
}

#d1['str'] = 'Agora ela existe'

d1.update({'nova_chave':'novo_valor'})

if d1.get('nova_chave') is not None:
     print(d1.get('nova_chave'))

#if d1.get('str') is not None:
 #    print(d1.get('str'))


# Para excluir alguma chave do dicionario
#exemplo
#del d1['str']


print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())

d1 = {
    'chave1': 'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla',
}

#print(len(d1))

# para d1.values() - você acessa os valores
# para d1.keys() - você acessa as chaves
# para d1.items() - você acessa as chaves e os valores ao mesmo tempo
# print(k[0], k[1])
#for k,v in d1.items():
#    print(k, v)

## Dicionários dentro de dicionários
clientes = {
    'cliente1': {
      'nome': 'Luiz',
       'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome':'Moreira',
    },
    'cliente3': {
        'nome':'Tiago',
        'sobrenome':'Duarte',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')



#d1 = {1: 'a', 2: 'b', 3: 'c'}
#v = d1

#print(d1)
#print(v)
# Sinal de igual eu não estou criando um novo objeto
# Os objetos são identicos
# Alterei o valor da chave 1 e os dois dicionarios mudaram
#v[1] = 'Luiz'

#print(d1)
#print(v)

d1 = {1: 'a', 2: 'b', 3: 'c'}

# Utilizando o copy eu estou escolhendo o outro endereço de mémoria
# Ao utilizar apenas v = d1, é como se eu estivesse utilizando o
# mesmo endereço por isso está errado.

v = d1.copy()
v[1] = 'Luiz'

print(d1)
print(v)


import copy


d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
#v = d1.copy()
v = copy.deepcopy(d1)

v[1] = 'Luiz'
#v['d'][0] = 'Joãozinho'
v['d'] = ('Otávio', 'Luiz')

print(d1)
print(v)





# fazer cast

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
# convertendo lista em dicionario(fazendo um cast)
# você pode fazer isso com tuplas tbm e vice-versa
d1 = dict(lista)
print(d1)

# funcao pop

d1 = {
    1: 2,
    2: 3,
    4: 5,
}
# para eliminar algum item eu posso usar
d1.pop(4)
print(d1)


# aqui ele elimina sozinho o ultimo item, precisa nem falar
d1.popitem()


# para concatenar os dicionarios

exemplo :

print(d1)
print(d2)

d1.update(d2) -- irá concatenar os dicionarios


"""

