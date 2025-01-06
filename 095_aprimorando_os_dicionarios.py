time = []
geral = {}
gols = []
totgols = 0

while True:
    geral['nome'] = input('Digite o nome do jogador: ')
    partidas = int(input('Quantas partidas ele jogou: '))
    for c in range(1, partidas + 1):
        g = int(input(f'Quantos gols ele fez na partida {c}: '))
        gols.append(g)
        totgols += g
    geral['gols'] = gols[:]
    gols.clear()
    geral['totgols'] = totgols
    totgols = 0
    time.append(geral.copy())
    user = input('Quer adicionr mais um jogador?[S/N]: ').upper().strip()[0]
    while user not in 'SN':
        print(f'ERRO...Digite apenas Sim ou Não.')
        user = input('Quer adicionr mais um jogador?[S/N]: ').upper().strip()[0]
    if user == 'N': 
        break
print('=-'*25)
print(f'Cod', end=' ')
for i in geral.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)
for i, j in enumerate(time):
    print(f'{i:<3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador(999 = break): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro...Digite um jogador valido\nNão temos jogador com o Cod. {busca}!')
        print('-'*50)
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time [busca] ['nome']}-- ')
        for i, g in enumerate(time [busca] ['gols']):
            print(f'No {i+1}° jogo fez {g} gols.')
        print('-'*50)
print(f'{'<< Volte Sempre >>':^50}')
