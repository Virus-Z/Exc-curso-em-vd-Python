def maior(lst):
    mai = 0
    tam = len(lst)
    for i, n in enumerate(lst):
        if i == 0:
            mai = n
        else:
            if mai < n:
                mai = n
    print(f'{'~'*25}')
    print(f'Analisando os valores passados...\n{lst}, foram informados um total de {tam} números\n E o maior deles foi: {mai}')
    print(f'{'~'*25}')


print(f'Digite alguns número que vou lhe falar qual foi o maior da lista e quantos números você me falou!')
lst = []
while True:
    while True:
        try:
            n = int(input('Digite um número: '))
            break
        except:
            print('Você não digitou um número inteiro valido, tente novamente!')
            continue
    lst.append(n)
    user = input('Gostaria de add mais um número?[S/N]: ').upper().strip()[0]
    while user not in 'SN':
        user = input('Gostaria de add mais um número?[S/N]: ').upper().strip()[0]
    if user == 'N':
        break
maior(lst)
