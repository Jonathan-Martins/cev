'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreo(com idade)
em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se
aposentar.'''
from datetime import date
ano_atual = date.today().year
trabalhador = {}

trabalhador['nome'] = str(input('Informe o nome: ')).strip()
ano_nasc = int(input('Informe o ano de nascimento: '))
trabalhador['idade'] = ano_atual - ano_nasc
trabalhador['ctps'] = int(input('Informe o nº da CTPS (0 se não tiver): '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Informe o ano de contratação: '))
    trabalhador['salario'] = float(input('Informe o salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - ano_atual) 
print('-'*50)
print(f'{"Resultados":^50}')
print('-'*50)
for k, v in trabalhador.items():
    print(f'{k}: {v}') 