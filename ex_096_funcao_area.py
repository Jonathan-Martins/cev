'''Faça um programa que tenha uma função chamada area(), que receba as dimensões
de um terreno retangular(largura e comprimento) e mostre a área do terreno.'''
def area(b, h):
    a = b * h
    print(f'A área de um terreno {b}x{h} é de {a:.2f}m².')

def cabecalho(titulo):
    print(f'{titulo:^30}')
    print('='*30)


cabecalho('Controle de Terreno')
comprimento = float(input('Por favor, informe o comprimento do terreno(m): '))
largura = float(input('Agora informe a largura(m): '))
area(comprimento, largura)