print('Gerador de PA - V2.0')
print('\033[1;31m='*20)
p = int(input('\033[mPrimeiro Termo: '))
r = int(input('Razão da PA: '))
x = p
c = 10
while not c == p:
    print('{}'.format(x), end=' => ' if p < c - 1 else ' = ')
    x += r
    p += 1
print('\033[1;31mFIM \033[mda \033[1;33mPA')