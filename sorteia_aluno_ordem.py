from random import shuffle

lista = []

for i in range(1, 5):
    lista.append(input('Informe um aluno: '))

print('Ordem de apresentação!')
shuffle(lista)
print(lista)