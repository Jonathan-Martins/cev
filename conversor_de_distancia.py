val = float(input('Informe uma distância em metros: '))

'''
print('{} convertidos para km são: {}'.format(val, (val/1000)))
print('{} convertidos para mi são: {:.3f}'.format(val, (val/1609.344)))
print('{} convertidos para hm(Hectômetro): {}'.format(val, (val/100)))
print('{} convertidos para dam(Decâmetro): {}'.format(val,(val/10)))
print('{} convertidos para dm(Decimetro): {}'.format(val, (val * 10)))
print('{} convertidos para cm(Centimetro): {}'.format(val, (val * 100)))
print('{} convertidos para mm(Milimetro): {}'.format(val, (val * 1000)))'''

print('{} m equivalem à: '.format(val))
print('{} km \n {:.2f} mi \n {} hm \n {} dam\n {} dm\n {} cm\n {} mm'.format((val/1000), (val/1609.344), 
    (val/100), (val/10), (val*10), (val*100), (val*1000)))