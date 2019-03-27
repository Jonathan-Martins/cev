'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados
b) Ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista'''
num = []
cont = 0

while True:
    val = int(input('Escreva um valor: '))
    num.append(val)
    print('Valor adicionado com sucesso!')
    cont += 1
    resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]
    if 'n' in resp:
        break
    elif 's' not in resp:
        print('Resposta invalida!')
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0]

if 5 in num:
    print(f'Encontrei o número 5!')
else:
    print('Não encontrei o número 5 :(')

num.sort(reverse=True)
print(f'Foram digitados {cont} números')
print(f'A lista em ordem crescente é {num}')