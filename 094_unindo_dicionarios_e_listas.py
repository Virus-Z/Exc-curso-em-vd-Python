geral = []
pessoa = {}
media = 0

while True:
    nome = input('Digite o nome do cliente: ')
    sexo = input('Digite o sexo [F/M]: ').upper().strip()[0]
    while sexo not in 'FM':
        print('Erro! Por favor digite "F" ou "M"')
        sexo = input('Digite o sexo[F/M]: ').upper().strip()[0]
    idade = int(input('Digite a idade: '))
    media += idade
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    geral.append(pessoa.copy())
    user = input('Gostaria de adicionar mais um cliente?[S/N] ').upper().strip()[0]
    while user not in 'SN':
        user = input('Gostaria de adicionar mais um cliente?[S/N] ').upper().strip()[0]
    if user == 'N':
        break
print('=-' * 20)
print(f'Foram cadastradas um total de {len(geral)} pessoas')
print(f'A idade media é de {int(media / len(geral))} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for c in geral:
    if c['sexo'] == 'F':
        print(f'{c['nome']};', end=' ')
print()
print(f'Listas das  pessoas que estão acima da média: ')
print('    ')
for c in geral:
    if c['idade'] >= media / len(geral):
        for k, v in c.items():
            print(f'{k}= {v};', end=' ')
        print()
        