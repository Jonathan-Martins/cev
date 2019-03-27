nome = input('Escreva seu nome completo: ')

print('Nome em maiusculo {}'.format(nome.upper()))
print('Nome em minusculo {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(" ",""))))

nome = nome.split()
print('Seu primero nome é {} e ele tem {} letras'.format(nome[0], len(nome[0])))

