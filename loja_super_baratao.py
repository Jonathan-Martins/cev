'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
a) Qual o total gasto na compra
b) Quantos produtos custam mais de R$ 1000
c) Qual é o nome do produto mais barato '''

total = cont = mais_barato = 0
produto = ' '
print('---------------------')
print('{:>^50}'.format(' LOJÃO TUDO BARATÃO '))
print('---------------------')
while True:
    print('---'*12)
    print('<--CADASTRAR COMPRA-->')
    print('---'*12)
    prod = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Informe o preço do produto: '))
    total += preco

    if preco > 1000:
        cont += 1
    
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        produto = prod
       

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    
    if op == 'N':
        print('---'*12)
        break
    else:
        print('---'*12)

print(f'Produto mais barato: {produto}', end=' -> ')
print(f'Preço: {mais_barato}')
if cont != 0:
    print(f'{cont} produtos acima de R$ 1000.00 ')   
print(f'Valor total: R$ {total:.2f}')