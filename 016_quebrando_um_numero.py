import math

n = float(input('Digite um numero quebrado: '))
q = math.trunc(n)
print('O numero digitado foi: {}, e sua porção inteira é: {}'.format(n, q))

from math import trunc

n = float(input('Digite um numero quebrado: '))
q = trunc(n)
print('O numero digitado foi: {}, e sua porção inteira é: {}'.format(n, q))

n = float(input('Digite um numero quebrado: '))
q = int(n)
print('O numero digitado foi: {}, e sua porção inteira é: {}'.format(n, q))

n = float(input('Digite um numero quebrado: '))
print('O numero digitado foi: {}, e sua porção inteira é: {}'.format(n, int(n)))
