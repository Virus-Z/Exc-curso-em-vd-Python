s = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma deles é: {}\nE o total de numeros encontrados foi: {}'.format(s,cont))
