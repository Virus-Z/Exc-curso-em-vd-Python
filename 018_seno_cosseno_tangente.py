import math
a = int(input('Digite um ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {}°, tem o seno de: {:.2f}\nO ângulo de {}°, tem o cosseno de: {:.2f}\nO ângulo de: {}°, tem a tangente de: {:.2f}'.format((a),s,(a),c,(a),t))

from math import sin,cos,tan,radians
a = int(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O angulo de: {}30°, tem o seno de: {:.2f}\nO ângulo de: {}°, tem o cosseno de: {:.2f}\nO ângulo de: {}°, tem a tangente de: {:.2f}'.format(a,s,a,c,a,t))

from math import sin,cos,tan,radians
a = int(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de: {}°, tem o seno de: {:.2f}'.format(a,s))
print('O ângulo de: {}°, tem o seno de: {:.2f}'.format(a,c))
print('O ângulo de: {}°, tem o seno de: {:.2f}'.format(a,t))
