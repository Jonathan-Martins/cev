nome = str(input('Escreva seu nome completo: ')).strip()

lista = nome.split()
print('Seu primeiro nome é {}'.format(lista[0]))

t = len(lista)
'''
marcador = 0
for i in range(0,t):
    marcador += 1

print('Seu ultimo nome é {}'.format(lista[marcador - 1])) 
'''
print('Seu ultimo nome é {}'.format(lista[t-1]))