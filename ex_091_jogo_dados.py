'''Crie um programa em que 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.'''
from random import randint
from operator import itemgetter
jogo = {'jogador1':randint(1,6), 'jogador2':randint(1,6), 'jogador3':randint(1,6),
        'jogador4':randint(1,6)}

ranking = []

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
#O método <sorted()> retornou uma lista com tuplas dentro por isso o uso do enumerate
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos')