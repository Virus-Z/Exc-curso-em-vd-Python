k = float(input('Qual seu peso: '))
a = float(input('Qual sua altura: '))
imc = k / a**2
print('Seu \033[1;36mIMC\033[m: {:.2f}'.format(imc))
if imc < 17:
    print('\033[1;31mPerigo!!!\n\033[mVocê está \033[1;31mMuito Abaixo \033[mdo peso!')
elif imc > 17 and imc <= 18.5:
    print('\033[1;31mCuidado!!\n\033[mVocê está \033[1;31mabaixo \033[mdo peso ideal!')
elif imc > 18.5 and imc <= 24.99:
    print('\033[1;33mParabéns!!\n\033[mVocê está no peso \033[32mideal\033[m!!')
elif imc > 25 and imc <= 29.99:
    print('\033[1;31mCuidado!!\n\033[mVocê está \033[1;31macima do peso \033[m!!!')
elif imc > 30 and imc <= 34.99:
    print('\033[1;31mCUIDADOO!!\n\033[mVocê já está no gral de \033[1;31mOBSIDADE 1 \033[m!!!!\nProcure um medico.')
elif imc > 35 and imc <= 39.99:
    print('\033[1;31mPerigo!!!\n\033[mVocê está no gral de \033[1;31mOBESIDADE 2 (SEVERA) \033[m!!!\nProcure um medico agora!')
else:
    print('\033[1;31mPERIGO EXTREMO!\n\033[mVocê está no gral de \033[1;31mOBESIDADE 3 (MÓRBIDA) \033[m!!!\nVa ao medico urgentee!!')