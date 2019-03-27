notas = [0]
soma = 0

for nota in range(1,5):
    notas.append(float(input('Digite a {} nota: '.format(nota))))
    soma = soma + notas[nota]
    
md = soma/nota

if md >= 7:
    print('Média: {} aluno aprovado sem exame!'.format(md))
elif md >= 4 and md < 7:
    print('Média: {} aluno em exame!'.format(md))
else:
    print('Média: {} aluno reprovado!'.format(md))