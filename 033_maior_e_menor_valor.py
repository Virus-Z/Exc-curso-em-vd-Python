p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
if p < s and p < t:
    m = p
if s < p and s < t:
    m = s
if t < s and t < p:
    m = t
if p > s and p > t:
    M = p
if s > p and s > t:
    M = s
if t > s and t > p:
    M = t
print('''O menor valor digitado foi: {}
O maior valor digitado foi: {}'''.format(m,M))

p = int(input('Primeiro número: '))
s = int(input('Segundo número: '))
t = int(input('Terceiro número: '))
m = p
M = p
if s < p and s < t:
    m = s
if t < p and t < s:
    m = t
if s > p and s > t:
    M = s
if t > p and t > s:
    M = t
print('''O menor valor digitado foi: {}
O maior valor digitado foi: {}'''.format(m,M))

p = int(input('Primeiro número: '))
s = int(input('Segundo número: ' ))
t = int(input('Terceiro número: '))
l = [p,s,t]
o = sorted(l)
print('''O menor valor digitado doi {}
O maior valor digitado foi: {}'''.format(o[0],o[2]))