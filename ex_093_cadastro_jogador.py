'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de 
gols feitos durante o campeonato.'''

jogador = {}
somagol = 0

jogador['nome'] = str(input('Nome: '))
jogador['quantidade de jogos'] = int(input(f'Quantos jogos {jogador["nome"]} jogou: '))
if jogador['quantidade de jogos'] != 0:
    jogador['jogos'] = []
    #print(jogador['jogos'])
    for i in range(jogador['quantidade de jogos']):
        jogador['jogos'].append(int(input(f'Gols na {i+1}ª partida: ')))
        #somagol += int(input(f'Gols na {i+1}ª partida: '))
        #somagol += jogador['jogos'][i]
    jogador['gols no campeonato'] = sum(jogador['jogos'])

print('-='*15)
print(f'{"ESTATÍSTICAS":^30}')
print('-='*15)
for k, v in jogador.items():
    print(f' -{k}: {v}')

print('-='*15)
print(f'{jogador["nome"]} fez {jogador["quantidade de jogos"]} jogo(s)')
for i in range(jogador['quantidade de jogos']):
    print(f'Na {i+1}ª partida {jogador["nome"]} fez {jogador["jogos"][i]} gol(s)')
print('-='*15)