from random import randint
computador = randint(0,10)
print('Pensei num número de 0 a 10, dúvido você adivinhar!')
jogador  = int(input('Em que número pensei: '))

tentativas = 0

while jogador != computador:
    if jogador > computador:
        print('Menos...')
    else:
        print('Mais...')
    
    jogador = int(input('Você errou! Escolha outro número: '))
    tentativas += 1
    

print('Parabéns! Eu realmente pensei no número {}. Você só precisou de {} tentativas pra adivinhar.'.format(jogador, tentativas))