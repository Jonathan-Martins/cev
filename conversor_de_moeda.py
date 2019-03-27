real = float(input('Quantos reais você tem?: '))

print('{:.2f} reais equivalem a {:.2f} dolares.'.format(real,(real/3.89)))

resp = input('Quer saber quanto equivale em euros também?(s/n) ')
if resp.lower() == "s":
    print('{:.2f} reais equivalem a {:.2f} euros.'.format(real, (real/4.45)))
elif resp.lower() == "n":
    pesoarg = input('E de pesos argentinos, tá afim de saber?(s/n)')
    if pesoarg.lower() == "s":
        print('{:.2f} reais equivalem a {:.2f} pesos argentinos.'.format(real, (real*9.55)))
    else:
        print('Ok. Obrigado!')
else:
    print('Ok. Obrigado!')
