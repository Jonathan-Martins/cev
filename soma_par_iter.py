soma = 0
for i in range(6):
    num = int(input('Escreva o {} número: '.format(i+1)))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares digitados é {}'.format(soma))

''' Somar os números pares entre os seis números inteiros digitados pelo usúario'''