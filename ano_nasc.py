from datetime import date 
ano = []
ano_atual = date.today().year
qtd_maiores = 0
qtd_menores = 0

for i in range(7):
    ano.append(int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1))))

for i in range(7):
    if ano_atual - ano[i] > 21:
        qtd_maiores += 1
    else:
        qtd_menores += 1

print('A quantide de menores é {} e de maiores é de {}'.format(qtd_menores, qtd_maiores))
    