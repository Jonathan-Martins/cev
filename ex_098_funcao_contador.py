'''Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: inicio, fim e passo. Seu programa tem que realizar três contagens
por meio da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def cabecalho(titulo):
    print('='* (len(titulo)+4))
    print(f'  {titulo}')
    print('='* (len(titulo)+4))

def contador(inicio, fim, passo):
            
    if inicio < fim:
        cabecalho('Contagem Progressiva!')
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for i in range(inicio, fim+1, passo):
            print(f'{i}', end='-> ', flush=True)
            sleep(0.5)
        print('FIM.')
    else:        
        if passo == 0:
            print(f'Não há como tirar 0 de um número! Contagem de {inicio} até {fim} de 1 em 1.')
            for i in range(inicio, fim-1, -1):
                print(f'{i}', end='-> ', flush=True)
                sleep(0.5)
            print('FIM.')
        elif passo < 0:
            print(f'Contagem de {inicio} até {fim} de {passo*(-1)} em {passo*(-1)}.')
            for i in range(inicio, fim-1, passo):
                print(f'{i}', end='-> ', flush=True)
                sleep(0.5)
            print('FIM.')
        else:
            cabecalho('Contagem regressiva!')
            print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
            for i in range(inicio, fim-1, passo*(-1)):
                print(f'{i}', end='-> ', flush=True)
                sleep(0.5)
            print('FIM.')


cabecalho('EX 098 - Contador')
contador(0, 10, 1)
contador(10, 0, 2)
cabecalho('Sua vez!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)