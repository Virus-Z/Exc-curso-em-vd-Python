n = (input('Informe um número: '))
print('''Analisando o número: {}
Unidades: {}
Dezenas: {}
Centenas: {}
Milhar: {}'''.format(n, n[3], n[2], n[1], n[0]))

n = int(input('Informe um numero: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('''Analisando o numero: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(n,u,d,c,m))

n = int(input('Informe um número: '))
print('''Analisando o número: {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(n,(n // 1 % 10),(n // 10 % 10), (n // 100 % 10), (n // 1000 % 10)))




