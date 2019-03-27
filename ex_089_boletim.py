'''Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
notas = []
aluno = []
media = []
soma = 0
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    notas.append(aluno[:])
    if aluno[1] == None:
        soma += aluno[1]
    else:
        soma += aluno[1] + aluno[2]
        media.append(soma/2)
        soma = 0

    aluno.clear()
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar? [s/n]: ')).strip().lower()[0]
    
    if resp == 'n':
        break


while True:
    print('>>>'*6, 'ALUNOS CADASTRADOS', '>>>'*6)
    print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
    print('-'*25)
    for pos, aluno in enumerate(notas):
        print(f'{pos:<4}{aluno[0]:<10}{media[pos]:>8.2f}')
    print('>>>'*6, 'FIM DO CADASTRO', '>>>'*6)

    nota = int(input('Quer ver as notas de quem? '))
    for pos, aluno in enumerate(notas):
        if nota == pos:
            print('>>>'*6,' BOLETIM' ,'>>>'*6)
            print(f'{"Nome:":<4} {aluno[0]:<10}')
            print(f'{"Nota 1:":<4} {aluno[1]:<10}')
            print(f'{"Nota 2:":<4} {aluno[2]:<10}')
            print(f'Média: {media[pos]:<10.2f}')
            print('>>>'*6, ' FIM DO BOLETIM ','>>>'*6)
        else:
            print(f'Valor inválido! {nota} não é um aluno cadastrado')
    
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [s/n]: ')).strip().lower()[0]
    if resp == 'n':
        print('Até mais. Volte sempre')
        break