frase = str(input('Escreva uma frase: ')).strip()

a = frase.lower().count('a')

print('Sua frase tem {} "As"'.format(a))
print('O primeiro "A" está na posição {}'.format(frase.lower().find('a')+1))
print('O ultimo "A" está na posição {}'.format(frase.lower().rfind('a')+1))