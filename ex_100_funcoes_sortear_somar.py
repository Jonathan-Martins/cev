'''Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
def cabecalho(titulo):
    print('='* (len(titulo)+4))
    print(f'  {titulo}')
    print('='* (len(titulo)+4))


def sorteia(lst):
    cabecalho('Função Sortear')
    print('Sorteando Números: ', end='')
    for i in range(5):
        lst.append(randint(0,5))
    for i in range(len(lst)):
        print(f'{lst[i]}', end=' ', flush=True)
        sleep(1)
    print('Pronto!')

def somaPar(lst):
    cabecalho('Função SomaPar')
    somap = 0
    print('Números pares da lista: ', end='')
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            print(f'{lst[i]} ', end='', flush=True)
            sleep(1)
            somap += lst[i]
    print()
    print(f'Soma dos números pares: {somap}') 
    
    

cabecalho('EX 100 - Funções de Sortear e SomarPar')

numeros = []
#sorteia(numeros)
#somaPar(numeros)
cabecalho('Não faz sentido')