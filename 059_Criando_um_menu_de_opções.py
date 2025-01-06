n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = False
while not s:
    print('''\033[mEscolha uma opção:
[1] somar
[2] multiplicar 
[3] maior
[4] novos números
[5] sair do programa''')
    r = int(input('Qual sua opção? '))
    if r == 1:
        x = n1 + n2
        print('R: A soma deles dara {}'.format(x))
        print('\033[1;33m*' * 20)
    elif r == 2:
        x = n1 * n2
        print('R: A multiplicação deles dara {}'.format(x))
        print('\033[1;33m*' * 20)
    elif r == 3:
        if n1 < n2:
            print('O número {} é o maior entre os 2 digitados'.format(n2))
            print('\033[1;33m*' * 20)
        else:
            print('O número {} é o maior entre os 2 digitados'.format(n1))
            print('\033[1;33m*' * 20)
    elif r == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
        print('\033[1;33m*' * 20)
    else:
        s = True
print('Tenha um ótimo dia!')