'''Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''
from random import sample
from time import sleep
numeros = []
jogos = []
val = 0
while True:
    val += 1
    numeros.append(val)
    if val > 59:
        break

val = int(input('Quantos palpites você deseja? '))    
for i in range(val):
    jogos.append(sample(numeros, 6))

print(f'Sorteando {val} jogos...')
for i, j in enumerate(jogos):
    j.sort()
    sleep(1)
    print(f'{i+1}º jogo: {j}')
print('Boa sorte!')
