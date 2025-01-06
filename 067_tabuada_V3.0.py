while True:
    print('~'*40)
    n = int(input('Digite um número para ver sua tabúada: '))
    print('~'*40)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} X {c:2} = {n*c:2}')
print('Programa tabúada encerrado! Volte sempre.')