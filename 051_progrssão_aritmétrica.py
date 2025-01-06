print('='*25)
print(f'{"10 TEMOS DE UMA PA":^25}')
print('='*25)
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p + 5 * r
for c in range(p,d,r):
    print('{}'.format(c), end=' -> ')
print('Acabouuu!')