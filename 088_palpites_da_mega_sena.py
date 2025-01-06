from random import randint
from time import sleep
l = []
c = c2 = 0
while True:
    try:
        r = input('Quantos jogos da mega você quer: ')
        rint = int(r)
        break
    except:
        print(f'OPS, parece que você não digitou um número valido, tente novamente!')
        continue
while c < rint:
    num = []
    while c2 < 6:
        r = randint(0,61)
        if r not in num:
            num.append(r)
            c2 += 1
        else:
            continue
    l.append(num[:])
    num.clear()
    c2 = 0
    c += 1
print('=-'*40)
for n, g in enumerate(l):
    print(f'jogo {n+1}: {g}')
    sleep(1)
print('=-'*40)

# from random import randint
# from random import shuffle
# megasena = list(range(0,61))
# print('-' * 30)
# print(f'{"JOGO DA MEGA SENA":^30}')
# print('-' * 30)
# pergunta = int(input('Quantos números quer que eu sorteie? '))
# for aposta in range(1, pergunta+1):
#     print(f'Jogo {aposta}: ', end='')
#     shuffle(megasena)
#     print(megasena[:6])
#     del(megasena[:6])