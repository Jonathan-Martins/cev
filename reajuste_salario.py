sal = float(input('Qual o salário do funcionário? '))
reaj = float(input('Qual a porcentagem de reajuste? '))

aum = (sal*reaj/100)

print('Com um aumento de {:.0f}% o salário de R$ {:.2f} subiu pra R$ {:.2f}'.format(reaj, sal, (sal+aum)))