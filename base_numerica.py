num = int(input('Escreva um número inteiro: '))

op = input("""Escolha uma das bases de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
0 - Sair """)

if op == '1':
    print('O número {} transformado em binário é {}'.format(num, bin(num)[2:]))
elif op == '2':
    print('O número {} transformado em octal é {}'.format(num, oct(num)[2:]))
elif op == '3':
    print('O número {} transformado em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Até mais...')


