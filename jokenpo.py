import  random
print('''JO KEN PO!
1) PEDRA
2) PAPEL
3) TESOURA  ''')

''' Pedra < Papel; Papel < Tesoura; Tesoura < Pedra; 
'''
items = ('pedra', 'papel', 'tesoura')
jogador = int(input('Escolha uma opção: '))
adversario = random.randint(0, 2)

if adversario == 0: #A máquina jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('OPÇÃO INVÁLIDA!')
elif adversario == 1: #A máquina jogou papel
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA!')
elif adversario == 2: #A máquina jogou tesoura
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('OPÇÃO INVÁLIDA!')
    
print('O computador escolheu {} e você {}'.format(items[adversario], items[jogador]))