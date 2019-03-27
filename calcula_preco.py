val= float(input('Qual o valor do produto? R$'))

fpag = input("Deseja pagar a vista ou a prazo?(v/p/x)")

if fpag.lower() == "v":
    print('Você tem direito a 15% de desconto!')
    print('O valor final do produto é R$ {:.2f}'.format(val-(val*15/100)))
    print('Obrigado pela compra. Volte sempre!')
elif fpag.lower() == "p":
    print('O produto sofre juros de 8%')
    print('O preço final será de {:.2f}'.format(val+(val*8/100)))
    print('Obrigado pela compra. Volte sempre!')
else:
    print('Ok. Obrigado!')