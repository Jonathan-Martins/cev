'''Crie um programa que tenha um tupla totalmente preenchida com uma contagem por
extenso, de zero até vinte. Seu programa deverá ler um num pelo teclado(0 a 20) e
mostrá-lo por extenso. '''

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte')
numext = ''


while True:
    num = int(input('Escreva um número(0 a 20): '))
    if 0 <= num <= 20:
        break

    print('Valor invalido! Tente novamente')    
print(f'Você digitou {extenso[num]}!')    
