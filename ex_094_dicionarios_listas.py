'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final,
mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade
c) Uma lista com as mulheres
d) Uma lista de pessoas com idade acima da média '''
pessoas = []
dic = {}
soma = 0

while True:
    dic['nome'] = str(input('Nome: ')).strip()
    dic['sexo'] = ' '
    while dic['sexo'] not in 'FM':
        dic['sexo'] = str(input('Sexo[F/M]: ')).strip().upper()[0]
        if dic['sexo'] not in 'FM':
                print('ERRO! Digite F ou M!')
    
    dic['idade'] = int(input('Idade: '))
    soma += dic['idade']
    pessoas.append(dic.copy())
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()[0]
        if resp not in 'sn':
                print('ERRO! Digite apenas s ou n!')
    if resp == 'n':
        print('Até mais...')
        break
'''
for i,p in enumerate(pessoas):
    soma += p["idade"]'''
media = soma/len(pessoas)

print('='*24)
print(f'{"RESULTADOS":^20}')
print('='*24)
print(f'=> Pessoas cadastradas: {len(pessoas)}')
print(f'=> Média de idade: {media:.2f} anos.')
print('=> Mulheres cadastradas:', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=', ')
print()
print('=> Pessoas com idade acima da média: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]}; {p["sexo"]}; {p["idade"]}', end='| ')
print()
print('='*24)
print(f'{"FIM":^20}')
print('='*24)