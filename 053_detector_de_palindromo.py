f = input('Digite uma frase: ').strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1, -1, -1):
    i += j[l]
if i == f:
    print('A palavra/frase digitada foi: {} e ela ao contrario é: {}'.format(f,i))
    print('Essa frase/palavra é sim um palindromo')
else:
    print('A palavra/frase digitada foi: {} e ela ao contrario é: {}'.format(f,i))
    print('Essa palavra/frase não é um palindromo')
