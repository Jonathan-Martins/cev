import math

ang= float(input('Diga o angulo: '))

sen = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}'.format(sen, coss, tang))
