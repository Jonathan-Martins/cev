'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor
lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
do fatorial. '''
def fatorial(num, show=False):
    '''
    Faz o fatorial de um número:
    param num: número o qual será descoberto o fatorial
    param show(opcional): booleano que indica se o processo de fatorial será mostrado
    return: retorna o resultado do fatorial do número informado
    '''

    c = num
    fat = 1

    if show == True:
        while c > 0:
            print(f'{c}', end='')
            print(' X ' if c > 1 else ' = ', end='' )
            fat *= c
            c -= 1

    if num == 0:
        fat = 1
        return fat
    else:
        while c > 0:
            fat *= c
            c -= 1
        return fat



resp = int(input('Informe o número: '))
visivel = str(input('Deseja ver a operação? (s/n): '))
if visivel == 's':
    re = True
elif visivel == 'n':
    re = False
else:
    print('Valor invalido! O programa vai quebrar')
print(fatorial(resp, re))
