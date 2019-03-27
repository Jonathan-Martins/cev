peso = []

for i in range(5):
    peso.append(float(input('Qual o {}º peso: '.format(i + 1))))

maior_peso = peso[0]
menor_peso = peso[0]
for i in range(5):
    if peso[i] > maior_peso:
        maior_peso = peso[i]
    
    if peso[i] < menor_peso:
        menor_peso = peso[i]

print('O maior peso é {:.2f} Kg'.format(maior_peso))
print('O menor peso é {:.2f} Kg'.format(menor_peso))