from random import randint
print('\033[1;31m=-'*10, end='')
print('\033[1;36m JOGO DO PAR OU IMPAR ', end='')
print('\033[1;31m-='*10)
c = 0
while True:
    pc = randint(1, 10)
    n = int(input('\033[mDigite um número de 1 a 10: '))
    if n not in range(1, 11):
        print('Número Invalido')
        break
    c += 1
    x = False
    while not x:
        r = input('Você escolher par ou impar? [P/I] ').strip().upper()[0]
        if r == 'P':
            x = True
        if r == 'I':
            x = True
    rc = ''
    t = n + pc
    if t % 2 == 0:
        rc = 'P'
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {t} e deu Par')
    else:
        rc = 'I'
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {t} e deu Ímpar')
    if rc != r:
        break
    else:
        print(f'Você \033[1;35mVenceuu!!!\n\033[mVamos jogar novamente...')
print(f'Você \033[1;31mPerdeuu!!\n\033[1;31mGAME OVER\n\033[mVocê venceu um total de {c} vezes.')

