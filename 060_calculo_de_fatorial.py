#Sem importação
n = int(input('Digite um número para calcular seu fatorial: '))
print('A soma do fatorial de {}! é: '.format(n), end='')
c = n
r = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print(r)

#Com importação
from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'. format(n, f))