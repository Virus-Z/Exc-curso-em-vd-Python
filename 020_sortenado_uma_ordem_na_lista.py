import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Teceiro nome: ')
n4 = input('Quarto nome: ')
n5 = input('Quinto nome: ')
l = [n1, n2, n3, n4, n5]
random.shuffle(l)
print('A ordem de apresentação será:\n{}'.format(l))

from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
n5 = input('Quinto nome: ')
l = [n1, n2, n3, n4, n5]
shuffle(l)
print('A ordem de apresentação será:\n{}'.format(l))