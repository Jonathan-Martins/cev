numero = int(input('Informe um número para o calculo do fatorial: '))
contador = numero
fat = 1
print('O fatorial de {}! = ' .format(numero), end='')
while contador > 0:
    print('{}'.format(contador), end ="")
    print(' X ' if contador > 1 else ' = ', end ="")
    fat *= contador
    contador -= 1

print('{}'.format(fat))
    
'''O contador é utilizado não só para indicar quando o loop acaba, mas também
os demais elementos do fatorial. a tag <end=''> indica que não haverá
quebra de linha na impressão. E no segundo <print> há um <if else> sobre o que 
será impresso a depender do valor do contador.'''
