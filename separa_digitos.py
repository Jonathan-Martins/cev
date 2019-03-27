num = input('Escreva um número: ')

mil = False
cen = False
dez = False
uni = False

print('Analisando o número...')
n = len(num)

if n == 4:
    mil = True
elif n == 3:
    cen = True
elif n == 3:
    dez = True
elif n < 2:
    uni = True

if n <= 2:
    #num = '0'.join(num)
    for i in range(2):
        num += '0'
    n = len(num)
    

#Separando o número algarismo por algarismo
alga = []
for i in range(n):
    alga.append(num[i])

print(alga)

if mil:
    print('O número tem {} milhar(es)'.format(alga[0]))
    print('O número tem {} centena(s)'.format(alga[1]))
    print('O número tem {} dezena(s)'.format(alga[2]))
    print('O número tem {} unidade(s)'.format(alga[3]))
elif cen:
    print('O número tem {} centena(s)'.format(alga[0]))
    print('O número tem {} dezena(s)'.format(alga[1]))
    print('O número tem {} unidade(s)'.format(alga[2]))
elif dez:
    print('O número tem {} dezena(s)'.format(alga[0]))
    print('O número tem {} unidade(s)'.format(alga[1]))
elif uni:
    print('O número tem {} unidade(s)'.format(alga[0]))
else:
    print('Você digitou um número invalido!')