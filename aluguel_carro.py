qtDias = int(input('Quantos dias de aluguel? '))
km = float(input('Quantos Km rodados? '))
#calculo do preço de aluguel
preco = (qtDias*60) + (km*0.15)

print('O valor total do aluguel é de R$ {:.2f}'.format(preco))