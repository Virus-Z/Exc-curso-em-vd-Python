"""c = - 1
t = - 999
n = 0
while n != 999:
    n = int(input('Digite um número (Caso queira parar digite: 999): '))
    t += n
    c += 1
print('O total de números digitados foi {}, e a soma entre eles dará: {}'.format(c,t))"""

n = t = c = 0
n = int(input('Digite um número (Caso queira encerrar digite \033[1;31m999\033[m): '))
while n != 999:
    t += n
    c += 1
    n = int(input('Digite mais um número (Caso queira encerrar digite \033[1;31m999\033[m): '))
print('Você digitou \033[1;36m{} \033[mnúmeros e a soma entre eles foi \033[1;33m{}'.format(c, t))
