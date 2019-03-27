'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares '''

a = tuple(int(input('Escreva um número: ')) for i in range(4))

print('----'*10)
print(f'Você digitou os valores {a}')
print(f'O número 9 apareceu {a.count(9)} vez(es)')
if 3 in a:
        print(f'O número 3 está na posição {a.index(3)+1}')
else:
        print('Número 3 não encontrado')        
print('Os números pares digitados são: ', end='')
for i in range(4):
    if a[i] % 2 == 0:
        print(f'{a[i]}', end=' ')
    


    