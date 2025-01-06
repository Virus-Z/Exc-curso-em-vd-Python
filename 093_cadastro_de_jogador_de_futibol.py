geral = {}
gols = []
totgols = 0

geral['nome'] = input('Digite o nome do jogador: ')
partidas = int(input('Quantas partidas ele jogou: '))
for c in range(1, partidas + 1):
    g = int(input(f'Quantos gols ele fez na partida {c}: '))
    gols.append(g)
    totgols += g
geral['gols'] = gols
geral['totgols'] = totgols
print('=-'*25)
print(geral)
print('=-'*25)
for k, v in geral.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*25)
print(f'O jogador {geral['nome']} jogou {partidas} partidas.')
for i, c in enumerate(gols):
    print(f'  => Na {i + 1}° partida, fez {c} gols.')
print(f'Foi um total de {totgols} gols.')
