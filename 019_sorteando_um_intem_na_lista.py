import random
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
n5 = input('Nome do quinto aluno: ')
l = [n1,n2,n3,n4,n5]
s = random.choice(l)
print('O aluno esclhido foi: {}'.format(s))

from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
n5 = input('Nome do quinto aluno: ')
l = [n1,n2,n3,n4,n5]
s = choice(l)
print('O aluno esclhido foi: {}'.format(s))