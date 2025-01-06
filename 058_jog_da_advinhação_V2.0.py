'''from random import randint
from time import sleep
s = str(randint(1, 10))
c = 0
print('Sou seu computador...\nAcabei de pensar em um numero entre 1 e 10.')
r = input('Será que você consegue adivinhar qual foi?\nQual é seu palpite? ')
print('processando...')
while r not in s:
    print('oPS, Você errou!')
    c += 1
    r = input('Qual é seu novo palpite? ')
print('Parabénss você acertouuu!\nVocê precisou de {} tentativas para acertar!'.format(c))
print('Sua escolha foi {}, e a do PC foi {}'.format(r,s))'''

from random import randint
from time import sleep
s = randint(1,10)
c = 0
ok = False
print('Sou seu computador...Acabei de pensar em um numero entre 1 e 10.')
print('Será que você conssegue acertar!?')
while not ok:
    r = int(input('Qual seu palpite? '))
    print('Processando...')
    sleep(1.5)
    c += 1
    if r == s:
        ok = True
    else:
        print('Você errou!')
        if r < s:
            print('OPS é um número mais alto')
        else:
            print('OPS é um número um pouco mais baixo')
print('Você acertou e precisou de {} tentativas, Parabénsss'.format(c))
