km = float(input('Informe a distancia em Km: '))

if km <= 200:
    preco = km * 0.50
    print('O valor da viagem é R$ {:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('O valor da viagem é R$ {:.2f}'.format(preco))