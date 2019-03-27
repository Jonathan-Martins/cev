cont = 0
soma_num = 0
flag = 0

print('Digite os números que deseja somar e escreva "999" quando estiver satisfeito')
while flag != 999:
    num = int(input('Escreva um número: '))
    flag = num
    if flag != 999:
        soma_num += num
        cont += 1
    else:
        print('Já vai? Até mais... ')
     

print('Você digitou {} números e a soma deles é {}'.format(cont,soma_num))