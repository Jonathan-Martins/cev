cidade = input('Digite o nome da cidade: ')

#print('Santo' in cidade)
if cidade[:5].lower().strip() == 'santo':
    print('Eu também. Faz tempo que não vou para lá!')
else:
    print('Mentiroso! Sei que tem Santo no nome!!!') 
