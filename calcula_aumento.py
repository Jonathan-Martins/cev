sal = float(input('Qual o salário? R$  '))

print('CALCULANDO AUMENTO... POR FAVOR AGUARDE...')
print('-==*==-'*12)
if sal > 1250:
    aumento = (sal*10)/100
    sal = sal + aumento
    print('Com o aumento de R$ {:.2f} seu salário vai para R$ {:.2f}'.format(aumento, sal))
else:
    aumento = (sal*15)/100
    sal = sal + aumento
    print('Com o aumento de R$ {:.2f} se salário vai para R$ {:.2f}'.format(aumento, sal))