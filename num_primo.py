num = int(input('Digite um número: '))
c = 0

for i in range(1, num+1):
    if num % i == 0:
        c += 1

    '''O contador armazena a quantidade de vezes em que o número foi divisivel e como os
    números primos tem por caracteristica ser apenas divisivel por ele mesmo e por 1, o limite 
    de divisões são duas. O limite para a duração do loop é o próprio número mais um, já que 
    para o python o ultimo valor é ignorado. Isso acontoce porque uma das formas de se verificar se
    um número é primo é sua sucessiva divisão. '''

if c == 2:
    print('O número {} é primo'.format(num))
else:
    print('O número {} não é primo'.format(num)) 