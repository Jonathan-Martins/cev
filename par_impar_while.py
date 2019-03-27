'''Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quano o jogador perder, mostrando o total
de vitórias consecutivas que conquistou ao final do jogo. '''

from random import randint

cont = soma = 0
print('<---PAR OU ÍMPAR?--->')
while True:
    jogador = int(input('Escreva um número: '))
    computador = randint(0, 10)
    soma = jogador + computador

    op = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}', end='...')
    if soma % 2 == 0:
        print('Par')
        if op == 'P':
            cont += 1
            print(f'Você venceu {soma} é par!')
        else:
            print(f'Você perdeu! Que pena... {soma} é par')
            break
    else:
        print('Ímpar')
        if op == 'I':
            cont += 1
            print(f'Você venceu {soma} é ímpar!')
        else:
            print(f'Você perdeu! Que pena... {soma} é ímpar')
            break

print(f'Você ganhou {cont} vezes.')