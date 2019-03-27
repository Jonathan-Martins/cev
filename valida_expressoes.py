'''Crie um programa em que o usuário digite uma expressão qualquer que use parênteses.
Seu app deverá analisar se a expressão está com os parenteses fechados e abertos na 
ordem correta'''
exp = []
'''
for i in range(1):
    val = str(input('Escreva algo: ' )).strip()
    exp.append(val)
'''
val = exp.append(input('Digite uma expressão: '))
print('Expressão: ', end="")
for x in exp:
    print(f'{x}',end=' ')


if '(' in exp:
    if exp.count('(') == exp.count(')'):
        print('\nExpressão válida!')
    else:
        print('\nExpressão inválida!')
else:
    print('\nA expressão não possui parênteses')

if exp[0].count('(') == exp[0].count(')'):
    print('\nExpressão válida')
else:
    print('\nExpressão inválida')