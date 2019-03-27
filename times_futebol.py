'''Cria uma tupla preenchida com a tabela do brasileirão na ordem de colocação. Depois mostre:
a) Os 5 primeiros times
b) Os 4 ultimos colocados
c) Times em ordem alfabética
d) Em que posição está a Chapecoense '''

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-Mg', 'Athletico-Pr',
        'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará',
        'Vasco', 'Sport', 'América-Mg', 'Vitória', 'Paraná')

print('-=-=-'*15)
print('{:^75}'.format('TABELA DO BRASILEIRÃO'))
print('-=-=-'*15)

print('-=-'*12)
print('Os cinco primeiros colocados: ', end='')
for t in range(0, 5 ):
    print(f'{times[t]}', end=', ')
print('CLASSIFICADOS PARA A LIBERTADORES!!')
print('-=-'*12)

print('-=-'*12)
print('Os quatro ultimos colocados são: ', end='')
for t in range(-4, 0):
    print(f'{times[t]}', end=', ')
print('REBAIXADOS!!')
print('-=-'*12)

print('-=-'*12)
print('Times em ordem alfabética: ', end='')
alfa = sorted(times)
for time in alfa:
    print(time, end=', ')
print('FIM')
print('-=-'*12)

print('-=-'*12)
chape = times.index('Chapecoense')
print(f'A Chapecoense é a {chape + 1}ª colocada')
print('-=-'*12)