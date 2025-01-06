x = 'Cadastre uma pessoa'
print('\033[1;31m~'*40)
print(f'\033[1;35m{x:^40}')
print('\033[1;31m~'*40)
t = h = m = 0
while True:
    i = int(input('\033[mIdade: '))
    if i >= 18:
        t += 1
    f = False
    while not f:
        s = input('Sexo [F/M] ').strip().upper()[0]
        if s == 'F':
            if i < 20:
                m += 1
            f = True
        if s == 'M':
            h += 1
            f = True
    f = False
    while not f:
        r = input('Gostaria de continuar? [S/N] ').strip().upper()[0]
        if r == 'S':
            f = True
        if r == 'N':
            f = True
    if r == 'N': 
        break
print('\033[1;31m~'*10,end='')
print(' \033[1;35mFim do Programa ', end='')
print('\033[1;31m~'*10)
print(f'\033[mTotal de pessoas com mais de 18 anos: {t}\nAo todo temos {h} homens cadastrados\nE temos {m} com menos de 20 anos.')
