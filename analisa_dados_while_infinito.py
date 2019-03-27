'''Crie um programa que leia a idade e o sexo de várias pessoas a cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos '''

contM = contH = cont18 = 0
print('-=-='*15)
print('ANALISADOR DE DADOS...')
print('-=-='*15)
while True:
    print('---'*12)
    print('CADASTRE UMA PESSOA')
    print('---'*12)
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo[F/M]: ')).strip().upper()

    if idade > 18:
        cont18 += 1
    
    if sexo == 'M':
        contH += 1

    if sexo == 'F' and idade < 20:
        contM += 1

    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]

    if resp == 's':
        print('---'*12)
    else:
        print('---'*12)
        break

print(f'Pessoas acima de 18 anos = {cont18}')
print(f'Homens cadastrados = {contH}')
print(f'Mulheres com menos de 20 anos = {contM}')