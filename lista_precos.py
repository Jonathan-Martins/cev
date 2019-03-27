'''Crie um programa que uma tupla única com nome de produtos e seus respectivos preços  na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular. '''

produtos = ('Lapis', 1.75, 'Caneta', 2.10, 'Apontador', 0.75, 'Caderno', 15.99, 'Livro', 35.40,
        'Compasso', 5.70, 'Mochila', 120.00)

tam = len(produtos)
'''
nome = 'Jonathan'
if type(nome) == str:
    print('Isso é uma string')
else:
    print('Não é bem assim que funciona!')
'''
print('-'*40)
print('<----LISTAGEM DE PREÇOS---->')
print('-'*40)
for i in range(0, tam):
    if type(produtos[i]) == str:
        print(f'{produtos[i]:.<30} R$ {produtos[i+1]:.2f}\n')
print('-'*40)