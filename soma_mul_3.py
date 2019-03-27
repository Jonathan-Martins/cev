soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 ==0:
        cont += 1
        soma += i

print(cont)
print('A soma dos números ímpares multiplos de 3 no intervalo entre 1 e 500 é {}'.format(soma))