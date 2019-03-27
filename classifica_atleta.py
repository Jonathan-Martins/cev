from datetime import date

ano_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Categorizando...')
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JÚNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')