'''Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma semelhante a  
função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.'''
def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            print('ERRO! Digite um número inteiro válido!')
        if ok:
            break
    return valor


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')
