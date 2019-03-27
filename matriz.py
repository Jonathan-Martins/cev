'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores válidos
lidos pelo teclado. No final, mostre a matriz na tela com a formatação correta.'''
matriz = [[], [], []]
val = 0
for i in range(9):
    val = int(input(f'Digite um valor: '))
    
    if i < 3:
        matriz[0].append(val)
    elif i < 6:
        matriz[1].append(val)
    else:
        matriz[2].append(val)

for mx in matriz:
    for i, m in enumerate(mx):
        if i < 2: 
            print(f'[{m:^5}]', end=' ')
        else:
            print(f'[{m:^5}]')
        