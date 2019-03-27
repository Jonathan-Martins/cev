num = int(input('Escreva o número: '))
r = int(input('Agora escrava a razão aritmética: '))

ultimo = num +(10-1)* r #Essa equação serve para devolver o enezimo elemento de uma PA
ultimo = ultimo + 1
for i in range(num, ultimo, r):
    print(i)
    

print('Razão aritmética = {}'.format(r))
