'''Crie um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma 
lista, no final mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves'''
pessoas = []
dados = []
cont = pesadas = leves = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:])
    #cont += 1
    dados.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar?[s/n] ')).strip().lower()[0]
    
    if 'n' in resp:
        break

#print(f'Foram cadastradas {cont} pessoas')
pesadas = leves = pessoas[0][1]
for p in pessoas:
    if p[1] > pesadas:
        pesadas = p[1]
    elif p[1] < leves:
        leves = p[1]

print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Maior peso: {pesadas}Kg. Mais pesados: ', end=' ')
for p in pessoas:
    if p[1] == pesadas:
        print(f'{p[0]}', end=', ')

print(f'\nMenor peso: {leves}Kg. Mais leves: ', end=' ')
for p in pessoas:
    if p[1] == leves:
        print(f'{p[0]}', end=', ')