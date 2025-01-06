p = int(input('Primeiro segmento: '))
s = int(input('Segundo segmento: '))
t = int(input('Terceiro segmento: '))
if p < s + t and s < p + t and t < p + s:
    if p == s == t:
        print('Os segmentos acima formam sim um triangulo, triangulo Equílatero.')
    elif p != s and s != t and t != p:
        print('Os segmentos acima formam sim um triangulo, triangulo Escaleno.')
    else:
        print('Os segmentos acima formam sim um triangulo, triangulo Isósceles.')
else:
    print('Os segmantos acima não podem formar um triangulo!')
