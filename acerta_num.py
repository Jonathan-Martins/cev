from random import randint

val = int(input('Informe um número entre 1 e 5: '))

num = randint(0, 5) # Atribui a variavel num um número inteiro aleatório entre 0 e 5

if val <= 5:
    if val == num:
        print('Parabéns!! Você acertou!!')
    else:
        print('Resposta errada! O número correto é {}'.format(num))
else:
    print('Número inválido!! Escolha um número entre 1 e 5')