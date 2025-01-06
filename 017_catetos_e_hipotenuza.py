import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co,ca)
print('A hipotenuza vai medir: {:.2f}'.format(h))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('COmprimento do cateto adjacente: '))
h = hypot(co,ca)
print('A hipotenuza vai medir: {:.2f}'.format(h))

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co**2+ca**2)**0.5
print('A hipotenuza vai medir: {:.2f}'.format(h))
