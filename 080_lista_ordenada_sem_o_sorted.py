l = []
for c in range(0,5):
    while True:
        try:
            n = int(input('Digite um número: '))
            break
        except:
            print('Você não digitou um número inteiro valido, tente novamente!')
            continue
    if c == 0 or n > l[-1]:
        l.append(n)
        print(f'Número adicionado ao final da lista com sucesso...')
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                print(f'Número adicionado a posição: {p}, com sucesso!')
                break
            p += 1
print(f'{l}')
