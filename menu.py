num1 = int(input('Escreva o primeiro número: '))
num2 = int(input('Escreva o segundo número: '))

print('O que deseja fazer?')
op = 0
novo = ''
while op != 5:
    print("""----MENU----
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR""")
    op = int(input('Selecione uma opção: '))
    
    if op != 5:
        if op == 1:
            soma = num1 + num2
            print('A soma entre {} e {} é {}'.format(num1,num2,soma))
            novo = str(input('Deseja escolher outra opção? [s/n] ')).strip().lower()
            if novo == 's':
                op = 0
            else:
                print('Ok. Tchau...')
                op = 5
        elif op == 2:
            soma = num1 * num2
            print('A multiplicação entre {} e {} é {}'.format(num1,num2,soma))
            novo = str(input('Deseja escolher outra opção? [s/n] ')).strip().lower()
            if novo == 's':
                op = 0
            else:
                print('Ok. Tchau... ')
                op = 5
        elif op == 3:
            soma = num1
            if soma < num2:
                soma = num2
            print('Maior número entre {} e {} é {}'.format(num1, num2, soma))
            novo = str(input('Deseja escolher outra opção? [s/n] ')).strip().lower()
            if novo == 's':
                op = 0
            else:
                print('Ok. Tchau... ')
        elif op == 4:
            print('Deseja informar novos números?')
            num1 = int(input('Escreva o primeiro número: '))
            num2 = int(input('Escreva o segundo número: '))
    elif op == 5:
        print('Finalizando...')
            
            

            