f = input('Digite uma frase: ').strip().lower()
s = f.find('e')+1
e = f.rfind('e')+1
print('''A letra 'e/E' aparece {}x na frase
A primeira letra 'e/E' apareceu na posição {}
A última letra 'e/E' apareceu na posição {}'''.format(f.count('e'),s,e))

f = input('Digite uma frase: ').strip().lower()
print("A letra 'e/E' aparece {}x na frase".format(f.count('e')))
print("A primeira letra 'e/E' aparece na posição {}".format(f.find('e')+1))
print("A última letra 'e/E' aparece na posição {}".format(f.rfind('e')+1))