from random import randint
from time import sleep
from operator import itemgetter

players = {'jogador-1' : randint(1, 6),
           'jogador-2' : randint(1, 6),
           'jogador-3' : randint(1, 6),
           'jogador-4' : randint(1, 6)}
Ranking = []
Ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('=-'*10,'VALORES SORTEADOS','=-'*10)
for k, v in players.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
print()
print('=-'*10,'Ranking','=-'*10)
for i, v in enumerate(Ranking):
    print(f'O {i+1}° lugar vai para o {v[0]}, que tirou {v[1]} no dado.')
    sleep(0.5)
