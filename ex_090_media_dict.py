'''Faça um programa que leia o nome e a média de um aluno, guardando também a 
situação em um dicionário. No final, mostre o conteúdo da estrutura na tela'''
from time import sleep
medias = {'aluno':' ', 'md': 0.0, 'situacao': ' '}

medias['aluno'] = str(input('Informe o nome: ')).strip()
medias['md'] = float(input('Informe a média: '))
if medias['md'] >= 7:
    medias['situacao'] = 'Aprovado!'
elif medias['md'] >= 5 and medias['md'] < 7:
    medias['situacao'] = 'em Recuperação!'
else:
    medias['situacao'] = 'Reprovado!'
print()
print('Analisando...') 
sleep(1)   
#print(f'Aluno {medias["situacao"]}')
print('-'*25)
for k, v in medias.items():
    print(f'- {k}: {v}')
    