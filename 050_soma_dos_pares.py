v = 0
c = 0
for w in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        v += n
        c += 1
print('A soma dos números pares digitados que foram {}, foi: {}'.format(c,v))