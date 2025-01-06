# l = []
# vmaior = []
# vmenor = []
# #Por que será que não funciona com o 0 em vez do -1?
# me = ma = -1
# for n in range(0, 5):
#     while True:
#         try:
#             x = (input(f'\033[mDigite um número inteiro na posição \033[1;33m{n}\033[m: '))
#             intX = int(x)
#             l.append(intX)
#             break
#         except:
#             print(f'Ops, você não digitou um número inteiro valido!\nVamos tentar novamente...')
#             continue
# for c in l:
#     if me and ma == -1:
#         me = ma = c
#     if me and ma != -1:
#         if c < me:
#             me = c
#         if c > ma:
#             ma = c
# for c, n in enumerate(l):
#     if n == ma:
#         vmaior.append(c)
#     if n == me:
#         vmenor.append(c)
# print(f'\033[mVocê digitou os seguintes valores: \033[1;31m{l}')
# print(f'\033[mO maior valor digitado foi \033[1;31m{ma}\033[m, na posição \033[1;33m{vmaior}')
# print(f'\033[mO menor valor digitado foi \033[1;31m{me}\033[m, na posição \033[1;33m{vmenor}\033[m')

# l = []
# vmaior = []
# vmenor = []
# me = ma = 0
# for n in range(0, 5):
#     while True:
#         try:
#             x = (input(f'\033[mDigite um número inteiro na posição \033[1;33m{n}\033[m: '))
#             intX = int(x)
#             l.append(intX)
#             if n == 0:
#                me = ma = intX
#             else:
#                 if intX > ma:
#                     ma = intX
#                 elif intX < me:
#                     me = intX
#             break
#         except:
#             print(f'Ops, você não digitou um número inteiro valido!\nVamos tentar novamente...')
#             continue
# for c, n in enumerate(l):
#     if n == ma:
#         vmaior.append(c)
#     if n == me:
#         vmenor.append(c)
# print(f'\033[mVocê digitou os seguintes valores: \033[1;31m{l}')
# print(f'\033[mO maior valor digitado foi \033[1;31m{ma}\033[m, na posição \033[1;33m{vmaior}')
# print(f'\033[mO menor valor digitado foi \033[1;31m{me}\033[m, na posição \033[1;33m{vmenor}\033[m')

l = []
me = ma = 0
for n in range(0, 5):
    while True:
        try:
            x = (input(f'\033[mDigite um número inteiro na posição \033[1;33m{n}\033[m: '))
            intX = int(x)
            l.append(intX)
            if n == 0:
               me = ma = intX
            else:
                if intX > ma:
                    ma = intX
                elif intX < me:
                    me = intX
            break
        except:
            print(f'Ops, você não digitou um número inteiro valido!\nVamos tentar novamente...')
            continue
print(f'\033[mVocê digitou os seguintes valores: \033[1;31m{l}')
print(f'\033[mO maior valor digitado foi \033[1;31m{ma}\033[m, na posição \033[1;33m',end='')
for i, n in enumerate(l):
    if n == ma:
        print(f'{i}...',end='')
print(f'\n\033[mO menor valor digitado foi \033[1;31m{me}\033[m, na posição \033[1;33m',end='')
for i, n in enumerate(l):
    if n == me:
        print(f'{i}...',end='')
print(f'\033[m')
