val = float(input('Informe o valor: '))
porc = int(input('Informe a porcentagem de desconto: '))
desc = (val*porc)/100

print('O valor do desconto de {}% é R$ {:.2f}.'.format(porc, desc))
print('O preço final é R$ {:.2f}'.format(val-desc))