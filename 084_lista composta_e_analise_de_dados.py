geral = []
galera = []
menor = maior = 0
while True:
    try:
        n = input('Digite o nome do cliente: ')
        p = input('Digite o peso em KG do cliente: ')
        pint = float(p)
    except:
        print("Por favor digite um número valido.\nVamos tentar de novo!")
        continue
    galera.append(n)
    galera.append(pint)
    geral.append(galera[:])
    galera.clear()
    r = input('Quer adicionar mais um cliente? [S/N]').upper().strip()[0]
    while r not in "SN":
        r = input('Quer adicionar mais um cliente? [S/N]').upper().strip()[0]
    if r == 'N':
        break
for p in geral:
    if menor == 0:
        menor = maior = p[1]
    else:
        if menor > p[1]:
            menor = p[1]
        if maior < p[1]:
            maior = p[1]
print('\033[1;35m=-'*50)
print(f'\033[mAo todo foram cadastradas {len(geral)} pessoas.')
print(f'O menor peso foi {menor} Kg, e são as pessoas: ',end='')
for p in geral:
    if p[1] == menor:
        print(f'{p[0]}',end='; ')
print(f'\nO menor peso foi {maior} Kg, e são as pessoas: ',end='')
for p in geral:
    if p[1] == maior:
        print(f'{p[0]}',end='; ')
