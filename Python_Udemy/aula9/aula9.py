"""
* Criar variáveis para nome(str),idade(int),
*altura(float) e peso(float) de uma pessoa
* criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa(baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais(peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings( com as chaves)

"""
nome = 'Tiago'
idade = 27
altura = 1.70
peso = 77.5
ano = 2021
ano_nascimento = (ano - idade)
imc = peso / (altura ** 2)

print(nome, 'nasceu em : ', ano_nascimento)
print(nome, 'tem o IMC:  ', round(imc, 2))
#  print(nome, 'tem o IMC: {:.2f} ' . format(imc))  # também pode ser utilizado

print(f'{nome} tem  {idade} anos e a sua altura é  {altura:.2f} . Seu ano de Nascimento foi {ano_nascimento} '
      f'e seu peso é exatamente {peso:.2f}. Seu IMC é igual a {imc:.2f}')



























