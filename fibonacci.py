print('-=-=' * 20)
qtde_elementos = int(input('Quantos elementos deseja ver? '))

n1 = 0
n2 = 1
cont = 0
n3 = 0

print('{} -> {}'.format(n1, n2), end=' -> ')
while cont < qtde_elementos:
    n3 = n1 + n2
    print('{} '.format(n3), end='-> ')
    n1 = n2
    n2 = n3
    cont += 1
print('FIM.')