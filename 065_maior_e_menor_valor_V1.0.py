c = s = t = me = ma = 0
r = 'S'
while r in 'S':
    n = int(input('Digite um número: '))
    c += 1
    t += n
    if c == 1:
        me = ma = n   
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    r = input('Quer continuar? [S/N] ').strip().upper()[0] 
m = t / c
print('Você digitou um total de {} números, a média deles dará {:.1f}\nO maior número digitado foi {}, e o menor {}.'.format(c, m, ma, me))
