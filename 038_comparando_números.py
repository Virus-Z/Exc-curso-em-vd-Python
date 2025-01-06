n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[1;35mPrimeiro \033[mnúmero e o maior.')
elif n1 < n2:
    print('O \033[1;35mSegundo \033[mnúmero é o maior.')
else:
    print('O números são \033[1;31mIguais!')
