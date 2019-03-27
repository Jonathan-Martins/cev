'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. '''

palavras = ('braco', 'tesouro', 'navio', 'rei', 'imperador', 'wano', 'capitulo', 'pirata',
            'ruivo', 'cortesa', 'cientista', 'doutora', 'computacao', 'coelho', 'velho',
            'cara', 'urso', 'prioridade')

for p in palavras:
    print(f'\nEm {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

'''As tuplas podem ser manipuladas como listas e como strings e de forma analoga, as strings caso 
componham listas ou tuplas também podem ser manipuladas como listas ou tuplas. '''