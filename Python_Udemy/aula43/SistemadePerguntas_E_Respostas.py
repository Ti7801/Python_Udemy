
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 6 * 5',
        'respostas': {
            'a': '5',
            'b': '12',
            'c': '30',
        },
        'resposta_certa': 'c',
    },
}
respostas_certas = 0

for pergunta_chave, pergunta_resposta in perguntas.items():
    print(f'{pergunta_chave}:{pergunta_resposta["pergunta"]}')

    for resposta_chave, resposta_resposta in pergunta_resposta['respostas'].items():
        print(f'[{resposta_chave}]:{resposta_resposta}')

    resposta_usuario = input('Digite a resposta: ')

    if resposta_usuario == pergunta_resposta['resposta_certa']:
        print(f'Você acertou!!')
        respostas_certas += 1
    else:
        print(f'Você errou!!!')

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou  {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')

