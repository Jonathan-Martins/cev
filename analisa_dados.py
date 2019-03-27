soma_idade = 0
cont_f = 0
idade_mais_velho = 0
nome_mais_velho = ''
pos = 0
for i in range(4):
    print('---{}ª PESSOA---'.format(i + 1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    if idade < 20 and sexo == 'f':
        cont_f += 1 
    
    if sexo == 'm' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
        
    soma_idade += idade



print('A média de idade do grupo é de {:.2f} anos'.format(soma_idade/4))
print('O homem mais velho do grupo é {} e ele tem {} anos'.format(nome_mais_velho, idade_mais_velho))
print('A quantidade de mulheres abaixo dos 20 anos é de {}'.format(cont_f)) 