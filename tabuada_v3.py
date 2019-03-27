'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o valor digitado pelo usuário for negativo. '''

print('-=-='*12)
print('Tabuada com <While True>')
print('-=-='*12)

while True:
    n = int(input('Qual tabuado deseja ver? '))
    if n < 0:
        print('Mas já?')
        break
    
    print('-'*10)
    for i in range(0, 11):
        print(f'{n} X {i:2} = {n * i}')
    print('-'*10)