from datetime import date
n = 0
v = 0
at = date.today().year
for c in range(1,8):
    a = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    m = a + 21
    if at < m:
        n += 1
    else:
        v += 1
print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade.'.format(v,n))
