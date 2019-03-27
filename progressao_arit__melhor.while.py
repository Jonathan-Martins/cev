num = int(input('Escreva um número: '))
r = int(input('Qual a razão aritmética? '))
cont = 1
elemento = num
termo = 0
mais = 10
print('Para o número {}, com a razão aritmética {} os 10 primeiros termos da progressão atitmética são:'.format(num,r))

#Whiles aninhandos
while mais != 0:
    termo = termo + mais
    while cont <= termo: 
        print('{} '.format(elemento), end='-> ')
        elemento +=  r
        cont += 1               
    print('PAUSA')
    mais = int(input('Quantos termos mais deseja ver? '))
print('Foram impressos {} termos'.format(termo))
print('FIM.')