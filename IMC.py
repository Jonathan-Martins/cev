from math import pow
print('CALCULADORA DE IMC')
peso = float(input('Qual seu peso? kg '))
alt = float(input('Qual sua altura? m '))

alt = pow(alt, 2)
imc = peso/alt

print('Seu Índice de Massa Corporal é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no seu peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')