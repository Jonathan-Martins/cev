'''nota1 = int(input('Digite a nota do primeiro semestre: '))
nota2 = int(input('Digite a nota do segundo semestre: '))

print('A média do aluno foi: {}.'.format((nota1+nota2)/2))'''
notas = [0]
soma = 0

for nota in range(1,5):
    #notas[nota] = int(input('Digite a {} nota: '.format(nota)))
    notas.append(float(input('Digite a {} nota:'.format(nota))))
    soma = soma + notas[nota]
    
'''for index, item in enumerate(notas):
        print(index, item)'''   

print('A média é {:.2f}'.format((soma/nota)))