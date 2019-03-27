'''Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista
única e mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente.'''
#As estruturas como listas podem ser declaradas dentro de outras listas
#Desde o ínicio do programa facilitando a estruturação dos dados
num = [[], []]
val = 0

for i in range(7):
    val = int(input(f'Digite o {i+1}º valor: '))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)

print(f'Números pares: {sorted(num[0])}')
print(f'Números ímpares: {sorted(num[1])}')

