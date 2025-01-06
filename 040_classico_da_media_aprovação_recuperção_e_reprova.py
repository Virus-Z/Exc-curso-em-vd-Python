n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3) / 3
if m > 6.5:
    print('\033[1;33mParabéns \033[msua medía foi {}, e você está \033[1;36mAPROVADO!!!'.format(m))
elif m <= 6.5 and m >= 5:
    print('''\033[1;31mCuidado!!!
\033[mVocê teve a media de: {}, e está de \033[1;33mRECUPERAÇÃO\033[m, estude!'''.format(m))
else:
    print('''\033[1;31mREPROVADO!!!
\033[mPoxa que pena você \033[1;31mNÃO \033[mfoi aprovado.
Sua media foi: {}'''.format(m))