cont = 0
soma_num = 0
media = 0
maior = 0
menor = 0
print('-=-='*12)
print('SOMA/MÉDIA/MAIOR/MENOR')
print('-=-='*12)
resp = str(input('Deseja começar as operações? [S/N] ')).strip().lower()

while resp == 's':
    num = int(input('Digite um número: '))
    cont += 1 
    soma_num += num

    if maior and menor == 0:
        maior = num
        menor = num

    if num > maior:
        maior = num

    if num < menor:
        menor = num
    
    resp = input('Deseja continuar? [S/N] ')

media = soma_num/cont
print('Você digitou {} números.'.format(cont))
print('Média = {}'.format(media), end=' -> ')
print('Maior = {}'.format(maior), end=' -> ')
print('Menor = {}'.format(menor))