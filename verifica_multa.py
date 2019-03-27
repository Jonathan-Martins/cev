from time import sleep

km = float(input('Informe a velocidade: '))

print('PROCESSANDO, AGUARDE...')
sleep(3)
if km > 80:
    print('Você foi multado!! Você excedeu o limite de 80km/h')
    multa = (km - 80) * 7
    print('O valor a pagar são R$ {:.2f}'.format(multa))
else:
    print('Você não tem multo alguma.')