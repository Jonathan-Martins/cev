num = []

for i in range(1, 4):
    num.append(int(input('Qual o {}º número? '.format(i))))

print(num)
maior = num[0]
menor = num[0]

for i in range(3):
    if maior < num[i]:
        maior = num[i]
    
    if menor > num[i]:
        menor = num[i]

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))