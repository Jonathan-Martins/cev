a = int(input('Informe um número: '))

def dob_tri_raiz(a):
    op = input('Você quer saber o dobro, o triplo ou raiz quadrada? (d/t/r)')
    if op.lower() == "d":
        print('O dobro de {} é {}'.format(a, (a*2)))
    elif op.lower() == "t":
        print('O triplo de {} é {}'.format(a, (a*3)))
    elif op.lower() == "r":
        print('A raiz quadrada de {} é {:.2f}'.format(a, (a**(1/2))))
    else:
        print('Opção inválida!!')

dob_tri_raiz(a)