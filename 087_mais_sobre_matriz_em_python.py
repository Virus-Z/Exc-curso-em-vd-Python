# lista = [[[], [], []], [[], [], []], [[], [], []]]
# Spares = S3col = maior2col = 0

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
#         if rint % 2 == 0:
#             Spares += rint
#         if n == 2:
#             S3col += rint
#         if cn == 1:
#             if n == 0:
#                 maior2col = rint
#             else:
#                 if maior2col < rint:
#                     maior2col = rint
# print('=-'*50)
# for g in lista:
#     for n in g:
#         print(n, end='')
#     print('')
# print('=-'*50)
# print(f'A soma de todos o números pares digitados dará: {Spares}')
# print(f'A soma de todos os numero da 3° coluna dará: {S3col}')
# print(f'O maior número da segunda coluna é o: {maior2col}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
gpares = col3 = maior2col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}:{c}]: '))
        if matriz[l] [c] % 2 == 0:
            gpares += matriz[l] [c]
        if c == 1:
            if l == 0:
                maior2col = matriz[l] [c]
            else:
                if maior2col < matriz[l] [c]:
                    maior2col = matriz[l] [c]
        if c == 2:
            col3 += matriz[l] [c]
print('=-'*50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()
print(f'A soma de todos o números pares digitados dará: {gpares}')
print(f'A soma de todos os numero da 3° coluna dará: {col3}')
print(f'O maior número da segunda coluna é o: {maior2col}')
