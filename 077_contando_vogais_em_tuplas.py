l = 'Bola', 'livro', 'Lapis', 'Pera', 'Uva', 'Carro', 'Bruxa', 'Vassoura'
for x in l:
    print(f'\n\033[mNa palavra \033[1;33m{x.upper()} \033[mtemos as seguintes vogais: ',end='')
    for p in x:
        if p.lower() in 'aeiou':
            print(f'\033[1;33m{p}',end='\033[m ')
print(f'\n','\033[1;31m*'*20, end=' ')
print(f'\033[1;36m{"FIM"}',end=' ')
print('\033[1;31m*\033[m'*20)
