num = int(input('Escreva um número: '))
r = int(input('Qual a razão aritmética? '))
cont = 10
elemento = 0
print('Para o número {}, com a razão aritmética {} os 10 primeiros termos da progressão atitmética são:'.format(num,r))
#Enquanto o elemento for diferente do elemento final da progressão o loop não acaba
while elemento != (num + (10-1)*r): 
    elemento = num + (10-cont)*r
    print('{} '.format(elemento), end='-> ')
    
    cont -= 1 
print('FIM.')