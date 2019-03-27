'''n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, s))

r = n1 / n2
print(r)

r = 3 * (5 + 52) **89 /7 -1 //9
print("o resultado dessa conta maluca ae é ", r)'''
n1 = int(input("digite um numero: "))
n2 = int(input("digite um outro numero: "))
s = n1 + n2
sub = n1 - n2
di = n1 / n2
mul = n1 * n2
pot = n1 ** n2
print("Os resultados da soma {}, subtração {} e multiplicação {}".format(s, sub, mul), end = ' ')
print("Os resultados da divisão {:.3f}, potencialção {} ".format(di, pot))