from random import randint
from time import sleep
print('\033[1;33m-='*10,end='')
print('\033[1;35m JA-KEN-PÔ ',end='')
print('\033[1;33m=-'*10)
print('\033[1;36mOpções:\n\033[m[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
e = int(input('Qual você escolhe: '))
if e >= 4 or e == 0:
    print('\033[1;31mOPÇÃO INVALIDA!!!')
else:
    l = ['','PEDRA','PAPEL','TESOURA']
    s = randint(1,3)
    print('\033[1;31mJA')
    sleep(0.5)
    print('\033[1;32mKEN')
    sleep(0.5)
    print('\033[1;34mPOO!!')
    sleep(0.75)
    print('\033[1;33m-='*25)
    print('\033[mEscolha do Computador: {}'.format(l[s]))
    print('Sua escolha: {}'.format(l[e]))
    print('\033[1;33m-=' * 25)
    if e == 1 and s == 3 or e == 2 and s == 1 or e == 3 and s == 2:
         print('\033[1;32mVOCÊ VENCEU!!')
    elif e == 1 and s == 2 or e == 2 and s == 3 or e == 3 and s == 1:
         print('\033[1;31mVOCÊ PERDEUU!!')
    else:
         print('\033[1;34mUAUU!! tivemos um empate!')
