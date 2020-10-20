import random

def generateAlphabets():
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    alfabeto = ''
    contador = 0

    while contador < 26:
        interador = random.randint(0,25)
        if char[interador] in alfabeto:
            pass
        else:
            alfabeto += char[interador]
            contador += 1
    return alfabeto

