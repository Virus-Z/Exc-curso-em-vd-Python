me = 0
m = 0
v = 0
mf = ''
no = ''
for p in range(1, 5):
   print('-'*5,'{}ª pessoa'.format(p),'-'*5)
   n = input('Nome: ').strip()
   i = int(input('Idade: '))
   s = input('Sexo [F/M]: ').strip().upper()
   m += i
   if i < 21:
       me += 1
   if i > v:
       no = n
       v = i
       mf = s
       if mf == 'M':
           hf = 'O Homen mais velho'
       else:
           hf = 'A mulher mais velha'
print('A média de idade do grupo é de {} anos'.format(m / 4))
print('{} tem {} anos e se chama {}'.format(hf, v, no))
print('Ao todo temos {} pessoas que não atingiram a maior idade.'.format(me))
