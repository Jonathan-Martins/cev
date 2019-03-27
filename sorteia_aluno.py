from random import choice

lista = []

for i in range(1, 5):
    lista.append(input('Digite o {}º nome da lista: '.format(i)))

print('O grande vencedor foi... {}'.format(choice(lista)))