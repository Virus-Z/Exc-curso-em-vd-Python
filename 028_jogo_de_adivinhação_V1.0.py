from random import choice
from time import sleep
print("""Ola seja bem vindo ao jogo de adivinhação de numeros!
O computador escolheu um numero de 1 a 5, tente adivinhar qual foi escolhido!""")
l = [1,2,3,4,5]
s = choice(l)
op = int(input('Escolha um numero de 1 a 5 e veja se acertou: '))
print('Processando...')
sleep(3)
print('o numero escolhido pelo PC foi: {}, já o seu foi: {}'.format(s,op))
if op == s:
    print('Otimo você acertou PARABÉNS!')
else:
    print('Poxa que pena, infelizmente você não acertou :(')

from random import randint
from time import sleep
pc = randint(1, 5) #Computador escolhe um numero!
print('-=-'*20)
print("""Ola seja bem vindo ao jogo de adivinhação de numeros!
O computador escolheu um numero de 1 a 5, tente adivinhar qual o foi escolhido!""")
op = int(input('Digite um numero de 1 a 5: ')) # o jogador tenta adivinhar!
print('Processando...')
sleep(3)
print('O numero escolhido pelo pc foi: {}, já o seu: {}'.format(pc,op))
if op == pc:
    print('Nice! você acertou!')
    print('-=-' * 20)
else:
    print('You lose! Que pena você errou.')
    print('-=-' * 20)
