'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estão na tupla '''
from random import sample

maior = menor = 0
numeros = tuple(sample(range(100), 5))
print(f'Números: {numeros}')

maior = menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    
    if n < menor:
        menor = n

print(f'Maior valor da tupla: {maior}\nMenor valor da tupla: {menor}')
'''
Para objetos iteraveis exitem dois métodos para retornar os valores máximo e mínimo
são eles: max(objeto) e min(objeto)'''