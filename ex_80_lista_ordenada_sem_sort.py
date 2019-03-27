'''Crie um program que leia cinco números e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela'''

lista = []
for c in range(5):
    n = int(input('Informe um valor: '))
    
    for i, v in enumerate(lista):
        if n < v:
            lista.insert(i, n)
            print(f'Adicionado na posição {i} da lista')
            break
    
    if len(lista) < c + 1:
        lista.append(n)
        print(f'{n} adicionado ao final da lista')
    
print(lista)

''' Nessa solução para cada valor dentro da lista testamos se o número lido é menor
que o valor da lista, se sim o inserimos na posição em que encontramos um valor maior que
o número lido. Já o ultimo <if> apenas testa se o tamanho da lista é menor que nosso laço mais um
, se sim o valor lido é adicionado ao fim da lista''' 