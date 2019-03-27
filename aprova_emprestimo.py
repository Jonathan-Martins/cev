preco_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o sálario? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

parcela = preco_casa / (anos * 12)

if parcela > (salario * 30) / 100:
    print('Infelizmente seu pedido foi \033[;31mNEGADO!')
else:
    print('Seu pedido foi \033[;32mAUTORIZADO!\033[m \nO valor da prestação será de R$ {:.2f}'.format(parcela))