from datetime import date
print('\033[1;33m-='*20)
print('\033[1;35mBEM-VINDOS A COMPETIÇÃO DE NATAÇÃO')
print('''\033[1;36mREGRAS:
\033[m* Ter idade entre 10 e 33 anos''')
print('\033[1;33m-='*20)
a = int(input('\033[mAno de nascimento: '))
y = date.today().year
c = y - a
if c <= 8:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mPRÉ-MIRIM'''.format(c))
elif c <= 10 and c >= 9:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mMIRIM'''.format(c))
elif c <= 12 and c >= 11:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mPETIZ'''.format(c))
elif c <= 14 and c >= 13:
    print('''O atleta tem {} anos.
\033[1;3333333mClassificação: \033[mINFANTIL'''.format(c))
elif c <= 16 and c >= 15:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mJUVENIL'''.format(c))
elif c <= 19 and c >= 17:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mJUNIOR'''.format(c))
elif c <= 25 and c >= 20:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mSENIOR'''.format(c))
elif c <= 35 and c >= 26:
    print('''O atleta tem {} anos.
\033[1;33mClassificação: \033[mMASTER'''.format(c))
else:
    print('\033[1;31mInfelizmente você não atende as regras  da competição, Desculpe!')
