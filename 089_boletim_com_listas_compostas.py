geral = []
while True:
    try:
        nome = input('Qual o nome do aluno? ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
    except:
        print('OPS, parece que você preencheu algo errado, vamos tentar novamente!')
        continue
    media = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], media])
    user = input('Quer adicionar mais um aluno? [S/N]').upper().strip()[0]
    while user not in 'SN':
        user = input('Quer adicionar mais um aluno? [S/N]').upper().strip()[0]
    if user == 'N':
        break
print('*'*40)
print(f'{'N°':<4}{'Nome':<8}{'Media':>27}')
print('*'*40)
for i, p in enumerate(geral):
    print(f'{i:<4}{p[0]:<8}{p[2]:>27}')
    print('-'*40)
print('*'*40)
while True:
    user = input('Digite o numero do aluno para ver mais detalhes sobre(Caso queira sair digite "s"): ').lower().strip()[0]
    if user == "s":
        break
    userint = int(user)
    if userint not in range(0, len(geral)):
        print('Você não digitou uma opção valida, vamos tentar novamente!')
        continue
    print(f'Aluno N°: {userint}\nNome do aluno: {geral[userint][0]}\nNotas do aluno: {geral[userint][1]}\nMedia: {geral[userint][2]}')
    print('-'*40)
