print('Gerador de PA - V2.0')
print('\033[1;31m='*20)
p = int(input('\033[mPrimeiro termo: '))
u = int(input('Digite o ultimo termo: '))
r = int(input('Razão da PA: '))
x = p
c1 = 0
c = 0
while u != 0:
    c1 = 0
    c += u
    while not c1 == u:
            print('{}'.format(x), end=' => ' if c1 < u - 1 else '\n')
            x += r
            c1 += 1
    u = int(input('Quantos termos você quer mostrar a mais? '))
print('\033[1;31mFIM \033[mda \033[1;33mPA\n\033[mCom {} termos no total'.format(c))

"""print('\033[1;31m='*20)
p = int(input('\033[mPrimeiro termo: '))
u = int(input('Digite o ultimo termo: '))
r = int(input('Razão da PA: '))
x = p
y = 1
t = 0
while u != 0:
    t += u
    while y <= t:
        print('{}'.format(x), end=' => ' if y < t else '\n')
        x += r
        y += 1
    print('PAUSA')
    u = int(input('Quantos termos você quer ver a mais: '))
print('\033[1;31mFIM \033[mda \033[1;33mPA\n\033[mA \033[1;33mPA \033[mteve {} termos no total.'.format(t))"""
