"""
add (adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets,
mas não em ambos)

"""
# Muito simililares a listas e tuplas e a dicionarios
# Não tem indices, não há como acessar um valor especifico diretamente
# do set
"""
#SE EU NÃO ADICIONAR VALORES AO SET S1, EU ESTOU CRIANDO UM DICIONÁRIO
EM BRANCO

s1 = {1, 2, 3, 4, 5}

print(s1)

for v in s1:
    print(v)
    
    
s1 = set()

s1.add(1)
s1.add(2)

# REMOVENDO O ELEMENTO 2 QUE EU ACABEI DE ADICIONAR
s1.discard(2)
    
s1 = set()
# aparece fora de ordem
#s1.update('Python')
s1.update([1, 2, 3, 4, 5], [5, 6, 7, 8])

print(s1)

    
# tira elementos duplicados você usa set
# você pode notar que l1 vai ignorar os repetidos 6.
l1 = [1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 1, 'LUIZ', 'LUIZ']
l1 = set(l1)# fiz um cast dessa lista no set, e ele removeu os duplicados
l1 = list(l1)

print(l1)

    # unindo todos os elementos
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2

print(s3)


# todos os elementos presentes nos dois conjuntos

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 & s2

print(s3)

# os elementos apenas dos sets da esquerda(o 7 é um exemplo)
# A ordem importa

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 - s2

print(s3)



# Elementos que estão nos dois sets em específico.
#Por exemplo: o 7 so ta no conjunto s1 e o 6 so ta no conjunto s2

s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 ^ s2

print(s3)

"""
# Se eu tenho varios elementos de uma lista duplicados e quero juntar
# as duas, eu posso fazer um set nas listas e tirar os elementos duplicados

l1 = ['Luiz', 'João', 'Maria']
l2 = ['Luiz', 'João', 'Maria', 'Luiz', 'Luiz', 'Luiz', 'Luiz',]

#l1 = list(set(l1))
#l2 = list(set(l2))

#print(l1, l2)

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')









