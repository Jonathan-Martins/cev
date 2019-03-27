s = str(input('Informe o sexo: [M/F] ')).strip().upper()
while s != 'M' and s != 'F':
    s = str(input('não é um dado válido. Por favor, informe o sexo novamente: ')).strip().upper()
print('{} foi cadastrado com sucesso!'.format(s))
