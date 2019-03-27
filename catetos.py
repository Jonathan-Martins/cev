import math

ops = float(input('Qual a medida do cateto Oposto? '))
adj = float(input('Qual a medida do cateto Adjacente? '))

hip = math.hypot(ops, adj)
print('O comprimento da hipotenusa com a função hypot {:.2f}'.format(hip))

hip2 = (math.pow(ops,2)) + (math.pow(adj,2))
print('-'*12)
print('O comprimento da hipotenusa sem a função hypot {:.2f}'.format(math.sqrt(hip2)))

hip3 = ops **2 + adj**2
print('-'*12)
print('O comprimento da hipotenusa sem o modulo math {:.2f}'.format(hip3**(1/2)))