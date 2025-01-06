l = []
while True:
    try:
        y = int(input(f'Digite um número inteiro: '))
    except:
        print(f'Ops, parece que você não não digitou um número inteiro!\nVamos tentar de novo...')
        continue
    if y not in l:
        l.append(y)
        print('Número adiconado com sucesso!')
    else:
        print('Número já existente na lista!')
    r = input('Gostaria de continuar?[S/N] ').upper().strip()[0]
    if r not in 'SN':
        while r not in 'SN':
            r = input('Gostaria de continuar?[S/N] ').upper().strip()[0]
    if r == 'N':
        break
l.sort()
print(f'{sorted(l)}')
