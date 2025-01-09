from random import randint

def sortear_numeros():
    lista = []
    for i in range(5):
        lista.append(randint(1, 60))
    return lista

print(f'Os números sorteados foram: {sortear_numeros()}')