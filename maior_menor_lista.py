'''Faça um programa que leia 5 valores e guarde-os numa lista. No final,
Mostre qual foi o maior e qual foi o menor valor digitado e as suas respectivas
posições na lista. '''
num = []

for i in range(5):
    num.append(int(input(f'Informe o {i+1}º número: ')))

print(f'Maior valor: {max(num)} -> Posições: ', end='')
for i, v in enumerate(num):
    if num[i] == max(num):
        print(f'{i}, ', end='')

print('\n')
print(f'Menor valor: {min(num)} -> Posições: ', end='')
for i, v in enumerate(num):
    if num[i] == min(num):
        print(f'{i}, ', end='')