'''Crie um programa em que o usuário possa digitar vários valores númericos  e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente. '''
valores = []


while True:
    val = int(input('Digite um valor: '))
    if val in valores:
        print('Valor repetido, manda outro!')
    else:
        valores.append(val)
    
    
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja continuar?[s/n]: ')).strip().lower()[0] 
    if resp == 'n':
        break

valores.sort()
print(valores)

'''O Segredo desse programa foi receber o valor por meio de uma váriavel, que eu chamei de 
"val", e com o método <append> recolhi o valor dessa váriavel apenas se o mesmo não existe
dentro da lista. O <append> pode ser usada não apenas para adicionar valores ao fim da lista 
direto do teclado, mas também de outras fontes como neste caso, de váriaveis. '''