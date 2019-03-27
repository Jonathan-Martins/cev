'''Aprimore o desafio anterior mostrando ao final:
a) a soma de todos os valores pares
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = s3 = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Informe o valor para a posição [{l} x {c}]: '))
'''A linha acima traz dois loops que populam a matriz '''
#maior = matriz[1][0]

print('{:^15}'.format('<-- MATRIZ -->'))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''A linha acima serve para imprimir a matriz com os resultados centralizados '''
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]        
        if c == 2:
            s3 += matriz[l][c]
        #if matriz[1][c] > maior:
        #    maior = matriz[l][c]
        if c == 0 or matriz[1][c] > maior:
            maior = matriz[1][c]
'''As linhas acima analisam os dados da matriz. O primeiro <if> soma os números pares, o segundo soma
apenas os valores da terceira coluna, e o ultimo seleciona o maior valor da segunda linha. '''   
print(f'A soma dos números pares da matriz é {soma}')
print(f'A soma dos números da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {maior}')