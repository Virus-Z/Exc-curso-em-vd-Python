from time import sleep
n = int(input('Digite um número inteiro: '))
print('Escolha umas das bases para conversão:')
print('''[1] Converter para \033[1;36mBINARIO
\033[m[2] Converter para \033[1;35mOCTAL
\033[m[3] Converter para \033[1;33mHEXADECIMAL''')
r = int(input('\033[mSua escolha: '))
print('\033[1;32mLoading...')
sleep(2.5)
if r == 1:
    print('\033[mO número {} convertido em \033[1;36mBINARIO \033[mé: {}'.format(n,bin(n)[2:]))
elif r == 2:
    print('\033[mO número {} convertido em \033[1;35mOCTAL \033[mé: {}'.format(n,oct(n)[2:]))
elif r == 3:
    print('\033[mO número {} convertido em \033[1;33mHEXADECIMAL \033[mé: {}'.format(n,hex(n)[2:]))
else:
    print('\033[1;31mOpção Invalida.')