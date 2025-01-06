s = m = b = 0
y = ''
x = 'LOJÃO DO VIRUz'
print('\033[1;31m~'*40)
print(f'\033[1;35m{x:^40}')
print('\033[1;31m~'*40)
while True:
    n = input('\033[mNome do produto: ')
    p = float(input('Preço: R$ '))
    s += p
    if p > 1000:
        m += 1
    if b == 0:
        y = n
        b = p
    if p < b:
        y = n
        b = p
    z = False
    while not z:
        r = input('Quer continuar? [S/N] ').strip().upper()[0]
        if r == 'S':
            z = True
        if r == 'N':
            z = True
    if r == 'N':
        break
print('\033[1;31m~'*10,end='')
print(' \033[1;35mFim do Programa ', end='')
print('\033[1;31m~'*10)
print(f'\033[mO total da compra foi R${s:.2f}.\nTemos {m} produtos custando mais de R$1000,00.\nO pruduto mais barato foi o(a) {y}, custando R${b:.2f}')