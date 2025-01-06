print('\033[1;33m=' * 40)
p = 'Banco Virus -Z'
print(f'\033[1;36m{p:^40}')
print('\033[1;33m=' * 40)
y = float(input('\033[mQual o valor do saque: R$'))
print('\033[1;36m~'*40)
while True:
    if y >= 200:
        duz = y // 200
        y -= duz * 200
        print(f'\033[mTotal de {int(duz)} cedulas de R$200.')
    elif y >= 100:
        cen = y // 100
        y -= cen * 100
        print(f'\033[mTotal de {int(cen)} cedulas de R$100.')
    elif y == 0:
        break
    elif y >= 50:
        cin = y // 50
        y -= cin * 50
        print(f'\033[mTotal de {int(cin)} cedulas de R$50.')
    elif y == 0:
        break
    elif y >= 20:
        vin = y // 20
        y -= vin * 20
        print(f'\033[mTotal de {int(vin)} cedulas de R$20.')
    elif y == 0:
        break
    elif y >= 10:
        dez = y // 10
        y -= dez * 10
        print(f'\033[mTotal de {int(dez)} cedulas de R$10.')
    elif y == 0:
        break
    elif y >= 5:
        cic = y // 5
        y -= cic * 5
        print(f'\033[mTotal de {int(cic)} cedulas de R$5.')
    elif y == 0:
        break
    elif y >= 2:
        doi = y // 2
        y -= doi * 2
        print(f'\033[mTotal de {int(doi)} cedulas de R$2.')
    elif y == 0:
        break
    elif y != 0:
        print(f'\033[1;31mAVISO: \033[mO valode de R${y:.2f} não pode ser sacado por não atingir o valor de cedula mínimo.')
        break
print('\033[1;33m=' * 40)
q = 'Volte sempre!!!'
print(f'\033[1;36m{q:^40}')
print('\033[1;33m=' * 40)
