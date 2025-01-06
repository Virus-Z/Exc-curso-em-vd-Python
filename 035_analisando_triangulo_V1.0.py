print('-=' * 19)
print('\033[1;35mAnalisador de Triângulo')
print('\033[0:m-=' * 19)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
l = [p, s, t]
o = sorted(l)
if o[0] + o[1] > o[2]:
    print('Os segmentos acima podem sim formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')


print('-=' * 19)
print('\033[1;36mAnalisador de Triângulo')
print('\033[0:m-=' * 19)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmanto: '))
if p < s + t and s < t + p and t < p + s:
    print('Os segmentos acima formam um triângulo!')
else:
    print('Os segmentos acima não formam um triângulo!')