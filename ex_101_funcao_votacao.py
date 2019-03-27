'''Crie um programa que tenha  uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL E OBRIGATÓRIO nas eleições.'''
#from datetime import date
def cabecalho(titulo):
    print('='* (len(titulo)+4))
    print(f'  {titulo}')
    print('='* (len(titulo)+4))


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    
    if  idade > 18 and idade < 65:
        return f'{idade} anos: voto OBRIGATÓRIO!'
    elif idade >= 65 or idade > 16 and idade <=18:
        return f'{idade} anos: voto OPCIONAL!'
    else:
        return f'{idade} anos: NÃO VOTA!'
    

cabecalho('EX 101 - Função voto()')
nasc = int(input('Em que ano você nasceu? '))
resp = voto(nasc)
print(resp)