# INTERANDO STRINGS COM WHILE EM PYTHON

#    Indices
#    0123456789....................................33


frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''  # Declarando uma string vazia


digito_usuario = input('Digite a letra que você quer mudar para maiusculo: ')

# Iteração <- Iterar
while contador < tamanho_frase:
    #print(frase[contador], contador)
    #nova_string += frase[contador]  # Aqui você está preenchendo a nova string com a string antiga em cada laço
    #print(nova_string)
    letra = frase[contador]
    if letra == digito_usuario:
        nova_string += digito_usuario.upper()  # upper utilizado para deixar a letra maiuscula
    else:
        nova_string += letra
    contador += 1

print(nova_string)








