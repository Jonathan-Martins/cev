'''Faça um programa que tenha uma funçao chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores 
e dizer qual deles é o maior.'''
def cabecalho(titulo):
    print('='* (len(titulo)+4))
    print(f'  {titulo}')
    print('='* (len(titulo)+4))
    

def maior_lst(lst):
    maior = lst[0]
    for n in lst:
        if n > maior:
            maior = n
    cabecalho('Resultados')
    print(f'Foram inseridos: {len(lst)} valores')
    print(f'Os valores inseridos foram: {lst}')
    print(f'Maior valor: {maior}')

def maior(*num):
    c = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')
        if c == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1
    print()
    cabecalho('Resultados')
    print(f'Foram inseridos {c} valores.')
    print(f'O maior valor é {maior}.')


cabecalho('Ex 099 - Função Maior Número')
num = []
while True:
    num.append(int(input('Escreva um número: ')))
    while True:
        resp = str(input('Deseja continuar? (s/n): ')).strip().lower()[0]
        if resp in 'sn':
            break
        else:
            print('ERRO! Valor inválido, digite apenas s ou n.')
    
    if resp == 'n':
        break
        
maior_lst(num)
maior(2, 4)
maior(1, 5, 7, 2, 3, 4, 8)