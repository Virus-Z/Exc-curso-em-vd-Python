n = int(input('Digite um número: '))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        cont += 1
        print('\033[1;33m',end=' ')
    else:
        print('\033[1;31m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi dividido {} vezes e por isso'.format(n,cont),end=' ')
if cont == 2:
    print('\033[1;35mÉ um numero primo')
else:
    print('\033[1;31mNão é um número primo')