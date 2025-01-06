print('\033[1;31m-'*10,end='')
print('\033[1;36m Sequência de Fibonacci ',end='')
print('\033[1;31m-'*10)
t = int(input('\033[mQuantos termos você que mostrar? '))
print('\033[1;31m~'*44)
t1 = 0
t2 = 1
c = 2
to = 0
print('\033[m{} {}'.format(t1,t2),end=' ')
while t != 0:
        while c < t:
                t3 = t1 + t2
                print('{}'.format(t3), end=' ')
                t1 = t2
                t2 = t3
                c += 1
        to += t
        c = 0
        t = int(input('\nQuantos numeros mais quer ver? '))
print('\n',end='\033[1;31m~'*44)
print('\n\033[1;35mFim\n\033[1;0mVocê solicitou \033[1;33m{} \033[mNúmeros da \033[1;36mSequência de Fibonacci'.format(to))
