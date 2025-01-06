l = float(input('Qual a largura da parede: '))
al = float(input('Qual a altura da parede: '))
a = (l*al)
print('Sua parede tem as seguintes dimenções: {:.2f}m X {:.2f}m, portanto sua área será: {:.2f}m².\nPara pintar essa parede, você precisará de {:.2f}L de tinta.'.format(l,al,a,(a/2)))

l = float(input('Qual a largura da parede: '))
al = float(input('Qual altura da parede: '))
a = (l*al)
t = a/2
print('Sua parede tem as seguintes dimenções: {:.2f}m X {:.2f}m, portanto sua área será: {:.2f}m²'.format(l,al,a))
print('Para pintar essa parede, você precisará de {:.2f}L de tinta.'.format(t))