l = []
c = 0
while True:
    try:
        n = int(input('Digite um número: '))
    except:
        print('Você não digitou um número inteiro valido, tente novamente!')
        continue
    if n == 5:
        c += 1
    l.append(n)
    while True:
        p = input('Quer ADD mais um número? [S/N] ').upper().strip()[0]
        if p in 'SN':
            break
    if p == 'N':
        break
print(f'Foram digitados {len(l)} números. {l}')
l.sort(reverse=True)
print(f'Segue a lista em ordem decrecente: {l}')
if c != 0:
    print(f'O número 5 foi digitado {c} vezes.')
else:
    print(f'O número 5 não foi digitado nem uma vez!')
