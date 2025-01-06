n = input('Qual seu nome completo? ').strip().lower()
t = 'silva' in n
print('Seu nome tem Silva?',t)

n = input('Qual seu nome completo? ').strip().title()
print('Seu nome tem Silva? {}'.format('Silva'in n))