# lista = [[[], [], []], [[], [], []], [[], [], []]]
# for cn, col in enumerate(lista):
#     for n, lin in enumerate(col):
#         while True:
#             try:
#                 r = input(f'Digite um número inteiro para a posição [{cn}:{n}]: ')
#                 rint = int(r)
#                 break 
#             except:
#                 print('Por favor digite um número inteiro!')
#                 continue
#         lin.append(rint)
# for g in lista:
#     for n in g:
#         print(n, end='')
#     print('')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}:{c}]: '))
print('=-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
