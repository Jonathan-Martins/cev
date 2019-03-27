num = int(input('De qual número deseja ver a tabuada?: '))

print('-'*15)
for i in range(0,11):
    print('{} x {:2} = {}'.format(num, i, (num*i)))
print('-'*15)
