'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.'''
jogador = []
dados = {}
gols = []
qtde_jogos = 0

while True:
    dados['nome'] = str(input('Nome: '))
    qtde_jogos = int(input(f'Quantidade de jogos de {dados["nome"]}: '))
    if qtde_jogos != 0:
        dados['gols'] = []
        for i in range(qtde_jogos):
            dados['gols'].append(int(input(f'Nº de gols na {i+1}ª partida: ')))
        gols.append(sum(dados['gols']))
    jogador.append(dados.copy())
    while True:
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('ERRO! Digite S ou N!')
    if resp == 'n':
        break

print(f'total de gols: {gols}')

while True:
    print('='*24)
    print(f'{"JOGADORES CADASTRADOS":^20}')
    print('='*24)
    print('cod', end=' ')
    for i in dados.keys():
        print(f'{i:<15}', end='  ')
    print()
    for pos, j in enumerate(jogador):
        print(f'=>{pos}: {j["nome"]:<15}')
    print('='*24)

    posicao = int(input('Qual jogador você deseja ver as estatísticas? '))
    for pos, j in enumerate(jogador):
        if posicao == pos:
            print('='*40)
            print(f'Estatísticas do jogador {j["nome"]}:')
            print('='*40)
            for k, v in j.items():
                print(f'=>{k}: {v}')
            print(f'=>Total de gols: {gols[pos]}')
            print('='*40)
        elif posicao >= len(jogador):
            print('Valor inválido, tente novamente!')
        
    
    while True:
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        print('Até mais')
        break