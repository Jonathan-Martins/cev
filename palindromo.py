frase = str(input('Escreva uma frase: ')).strip().upper()

invertido = ''
for letra in frase:
    if letra != " ":
        invertido = letra + invertido
'''Esse <for> tem como função inverter as letrar da frase informada. Para tal, ele
verifica por meio do <if> em seu interior se cada caracter designado por <letra> é diferente
de um espaço vazio, se o for esse caracter será adicionado a variavel <invertido>.'''

#Essa instrução remove os espaços vazios da frase original para que a comparação possa ser feita
frase = frase.replace(' ','')
'''Outra forma de desconsiderar os espaços seria
frase.split() para separar as palavras pelos espaços
frase = "".join(frase) para reconecta-las sem os espaços'''
print(frase)       
print(invertido)

if invertido == frase:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo!')

