alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z",]

def ENCvigenere(entrada, chave):
    entrada = entrada.lower()
    nova_string = ''
    ponteiro = 0
    for c in entrada:
        if ponteiro > len(chave) -1:
            ponteiro = 0
        interador = alfabeto.index(c)
        k = alfabeto.index(chave[ponteiro])
        numero = (interador + k) % 26
        ponteiro += 1
        interador = alfabeto[numero]
        nova_string += interador
    return nova_string

