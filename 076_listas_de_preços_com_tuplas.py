l = 'Caderno', 5, 'Lapis', 1.5, 'Borracha', 15, 'Mochila', 69.90, 'Livro', 10, 'Regua', 4.5
print('\033[1;33m-='*25)
print(f'\033[1;36m{"Tabela de Valores":^50}')
print('\033[1;33m-='*25)
for c in l:
    if type(c) != int and type(c) != float:
        print(f'\033[m{c:.<35}',f'R$ {l[l.index(c)+1]:>5.2f}')
print('\033[1;33m-='*25)
