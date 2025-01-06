from random import randrange
c = 0
me = 0
ma = 0
print('os N° sorteados foram: ',end=' ')
while c <+ 5:
    s = randrange(1,100)
    print(s,end=' ')
    if c == 0:
        me = s
        ma = s
    if c != 0:
        if ma > s:
            ma = s
        elif me < s:
            me = s
    c +=1
print(f'\nO maior número sorteado foi: {ma}\nO menor número sorteado foi: {me}')
