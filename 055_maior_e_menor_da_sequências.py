pe = 0
le = 0
for c in range(1,6):
    p = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        pe = p
        le = p
    else:
        if p > pe:
            pe = p
        if p < le:
            le = p
print('O maior peso inscrito foi: {}Kg\nO menor peso inscrito foi: {}Kg'.format(pe,le))

#Gambiarra

'''p = 0
l = 1000
for c in range(1,6):
    pe = float(input('Peso da {}ª pessoa: '.format(c)))
    if pe > p:
        p = pe
    elif pe < l:
        l = pe
print('O maior peso inscrito foi: {}Kg\nO menor peso inscrito foi: {}Kg'.format(p,l))'''