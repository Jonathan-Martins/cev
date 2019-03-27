print('Vamos calcular quanta tinta precisamos pra pintar a parede?')
alt = float(input('Qual a altura da parede?: '))
lar = float(input('Qual a largura da parede?: '))
mquad = lar*alt

print('A área da parede é de {}m²'.format(mquad))
print('Para esse tamanho de parede você precisa de {}L de tinta.'.format(mquad/2))