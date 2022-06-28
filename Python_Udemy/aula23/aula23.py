"""
For in em Python
Iterando strings com for
Função range(start=0,stop, step=1)
"""

"""
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
    
texto = 'Python'

for letra in texto:
    print(letra)
    
for numero in range(0, 100, 8):
    print(numero)

for n in range(100):
    if n % 8 ==0:
        print(n)   
            
texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço(finaliza)

for letra in texto:
    if letra == 't':
        continue  # PULAR PARA O PROXIMO LAÇO
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break  # TERMINAR O LAÇO E NÃO CONTINUAR EXECUTANDO
    else:
        nova_string += letra
        
        
 texto = 'Tiago estuda Engenharia Elétrica no IFPB'

letra_digitada = input('Digite qual letra você irá transoformar para maiuscula: ')

for letra_digitada in texto:
    if letra_digitada == 'e':
        print(letra_digitada.upper())
    


       
        

"""




