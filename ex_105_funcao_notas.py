'''Faça um programa que tenha uma função chamada notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação da turma(Opcional)
Adicione as docstrings da função'''
def notas(*nota, sit=False):
    '''
    Função para calcular as notas dos alunos de uma turma
    param *nota: desempacota as notas de vários alunos
    param sit: Recebe um valor lógico, True ou False, que sinaliza se a
    situação da turma deve ser exibida ou não
    return: retorna um dicionário com a maior nota da turma, a menor nota,
    a média da turma e a situação da mesma caso o param sit seja marcado como True.
    '''
    
    turma = {}
    maior = menor = soma = 0
    '''
    for i, n in enumerate(nota):
        turma[f'nota{i+1}'] = n
    '''
    maior = menor = nota[0]
    for n in nota:
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    
    turma['maior-nota'] = maior
    turma['menor-nota'] = menor
    turma['media'] = soma / len(nota)
    if sit == True:
        if turma['media'] >= 7:
            turma['situacao'] = 'Ótima'
        elif turma['media'] < 7 and turma['media'] >= 4:
            turma['situacao'] = 'Mais ou menos'
        else:
            turma['situacao'] = 'Ruim'
    return turma



    
print(notas(6, 8, 6, 7.5, sit=True))
help(notas)