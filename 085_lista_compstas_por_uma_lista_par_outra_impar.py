núm = [[], []]
c = 1
while c <= 7:
    try:
        n = input(f'Digite o {c}° número: ')
        Nint = int(n)
    except:
        print('Digite um número inteiro por favor.\nVamos tentar novamente!')
        continue
    if Nint % 2 == 0:
        núm[0].append(Nint)
    else:
        núm[1].append(Nint)
    c += 1
núm[0].sort()
núm[1].sort()
print('=-'*50)
# print(geral)
print(f'os valores pares digitados foram: {núm[0]}')
print(f'os valores impares digitados foram: {núm[1]}')
