"""
For/ Else em Python

#
"""
# O FOR TBM POSSUI AS PALAVRAS BREAK E CONTINUE TBM
"""

for valor in variavel:
    print(valor)
    # break e continue
    print(valor)


for valor in variavel:
    if valor.startswith('J'):   #  checa se  uma string que estou testando começa com determinada letra
        print('Começa com J', valor)
    else:
        print('Não começa com J!!', valor)
        

variavel = ['Luiz Otávio', 'Joãozinho', 'Marilia']

comeca_com_j = False

for valor in variavel:                  # Se o j ja for minuscula ele irá continuar minusculo
    if valor.lower().startswith('j'):  # Adicionando lower() ele converte para o minusculo a letra maiuscula
        break
#        comeca_com_j = True
#  if comeca_com_j:
#    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J')



for valor in variavel:                  # Se o j ja for minuscula ele irá continuar minusculo
    if valor.lower().startswith('j'):  # Adicionando lower() ele converte para o minusculo a letra maiuscula
        continue
    print(valor)    
#        comeca_com_j = True
#  if comeca_com_j:
#    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J')


        
"""








