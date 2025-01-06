n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais número: ')),
     int(input('Digite o ultimo número: ')))
print(f'\nOs números digitados foram: {n}')
print(f'\nO número nove aprece {n.count(9)} vezes.')
if 3 in n:
    print(f'\nO número três aparece na posição: {n.index(3)+1}')
else:
    print(f'\nO número três não foi digitado nem uma vez.')

print(f'\nO números pares digitados foram: ',end='')
for c in n:
    if c % 2 == 0:
        print(c,end=' ')
print('\nFim')
