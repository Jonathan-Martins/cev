'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer 
como parâmetro e mostre uma mensagem com tamanho adaptavel.'''
def cabecalho(titulo):
    print(f'{titulo:^30}')
    print('='*30)

def escreva(txt):
    print('='*(len(txt)+4))
    print(f'  {txt}')
    print('='* (len(txt)+4))


cabecalho('String Variavel?')
texto = str(input('Escreva algo: ')).strip()
escreva(texto)