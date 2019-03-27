a = float(input('Qual o primeiro segmento? '))
b = float(input('Qual o segundo segmento? '))
c = float(input('Qual o terceiro segmento? '))

'''
Para determinar se um segmento está apto a formar um triangulo ele deve atender as seguintes condições:
1 - Ele deve ser maior que a diferença absoluta entre os dois outros segmentos, ou seja, o módulo dessa diferença
2 - Ele deve ser menor que a soma dos demais segmentos.
|b - c| < a < b + c
'''

if abs(b - c) < a and a < b + c:
    if abs(a - c) < b and b < a + c:
        if abs(a - b) < c  and c < a + b:
            print('Os segmentos formam um \033[1;32mtriângulo!\033[m')
else:
    print('Os segmentos não podem formar um \033[1;31mtriângulo! :(\033[m')