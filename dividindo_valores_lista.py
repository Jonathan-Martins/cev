'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados.
Ao final, mostre o conteúdo das três listas geradas.'''
lista1 = []
#populando a 1ªlista
while True:
    val = int(input('Escreva um valor: '))
    lista1.append(val)
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar?[s/n] ')).strip().lower()[0]
    
    if 'n' in resp:
        break

pares = []
impares = []
tam = len(lista1)
#Separando pares de impares
for i in range(0, tam):
    if lista1[i] % 2 == 0:
        pares.append(lista1[i])
    else:
        impares.append(lista1[i])

print(f'Lista com todos os números: {lista1}')
print(f'Lista dos números pares: {pares}')
print(f'Lista dos números ímpares: {impares}')