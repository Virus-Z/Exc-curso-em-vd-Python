# l = []
# lp = []
# li = []
# user = ''
# while True:
#     try:
#         user = input('Digite um número inteiro: ')
#         intL = int(user)
#     except:
#         print(f'Ops, parece que você não digitou um número valido.\nVamos tentar novamente!')
#         continue
#     l.append(intL)
#     if intL % 2 == 0:
#         lp.append(intL)
#     if intL % 2 != 0:
#         li.append(intL)
#     while True:
#         p = input('Quer ADD mais um número? [S/N] ').upper().strip()[0]
#         if p in 'SN':
#             break
#     if p == 'N':
#         break
# print(f'Aqui está  a lista formada: {l}')
# print(f'Agora apenas os números pares: {lp}')
# print(f'E por ultimo os números impares: {li}')

l = []
lp = []
li = []
user = ''
while True:
    try:
        user = input('Digite um número inteiro: ')
        n = int(user)
    except:
        print(f'Ops, parece que você não digitou um número valido.\nVamos tentar novamente!')
        continue
    l.append(n)
    while True:
        p = input('Quer ADD mais um número? [S/N] ').upper().strip()[0]
        if p in 'SN':
            break
    if p == 'N':
        break
for n in l:
    if n % 2 == 0:
        lp.append(n)
    if n % 2 != 0:
        li.append(n)
print(f'Aqui está  a lista formada: {l}')
print(f'Agora apenas os números pares: {lp}')
print(f'E por ultimo os números impares: {li}')
