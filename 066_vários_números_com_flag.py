s = c = 0 
while True:
    n = int(input('Digite um número: (Digite 999 para finalizar) '))
    if n == 999:
        break
    s += n
    c += 1 
print(f'Você digitou um total de {c} números, a soma de todos eles dará {s}')
