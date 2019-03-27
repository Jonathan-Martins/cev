from datetime import date

ano_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
#aux = idade - 18


if idade < 18:
    aux = 18 - idade
    ano_alis = aux + idade + ano_nasc
    print("""Você ainda não tem idade para o serviço militar obrigatório. Porém falta(m)
    {} ano(s). O ano do seu alistamento será {}""".format(aux, ano_alis))
elif idade > 18:
    aux = idade - 18
    ano_alis = ano_atual - aux
    print("""Você tem mais de 18 anos. Seu  alistamento foi a {} ano(s) em {}, se ainda não se alistou,
    procure uma junta do serviço militar urgente!!!""".format(aux, ano_alis))
else:
    print('Este é o ano em que você deve fazer o alistamento obrigatório.')
