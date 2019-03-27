'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio,
pergunte ao usuário qual será o valor a ser sacado(num inteiro) e o programa vai
informar quantas cédulas de cada valor serão entregues.
considerando notas de 50, 20, 10 e 1. '''

notas50 = notas20 = notas10 = notas1 = totalnotas = valor = 0
print('-=-='*10)
print('{:^30}'.format('Banco de teste'))
print('-=-='*10)
while True:
    saque = int(input('Quanto deseja sacar? R$ '))
    valor = saque
    
    while valor > 50:
        valor -= 50
        notas50 += 1 
    
    while valor > 20:
        valor -= 20
        notas20 +=1

    while valor > 10:
        valor -= 10
        notas10 += 1

    while valor >= 1:
        valor -= 1
        notas1 += 1
    
    if valor == 0:
        break
    
    
print(f'Notas de R$ 50,00: {notas50}')
print(f'Notas de R$ 20,00: {notas20}')    
print(f'Notas de R$ 10,00: {notas10}')
print(f'Notas de R$ 1,00: {notas1}')
