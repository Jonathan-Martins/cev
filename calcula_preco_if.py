preco = float(input('Qual o preço do produto? '))

print("""Formas de pagamento
1- À vista dinheiro/cheque
2- À vista no cartão
3- Em 2x no cartão
4- 3x ou mais no cartão """)

fpag = input('Escolha uma opção: ')
if fpag == '1':
    print('Você ganhou 10% de desconto!!')
    print('Valor total da compra: R$ {:.2f}'.format(preco-(preco*10)/100))
elif fpag == '2':
    print('Você ganhou 5% de desconto!!')
    print('Valor total da compra: R$ {:.2f}'.format(preco-(preco*5)/100))
elif fpag == '3':
    parcela = preco/2
    print('Sua compra será dividida em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
    print('Valor total da compra: R$ {:.2f}'.format(preco))
else:
    totalparc = int(input('Quantas parcelas? '))
    preco = preco + (preco*20)/100
    parcela = preco/totalparc
    print('Sua compra será dividida em {}x de R$ {:.2f} COM JUROS'.format(totalparc, parcela))
    print('Valor total da compra: R$ {:.2f}'.format(preco))