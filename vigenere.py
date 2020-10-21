alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z",]

def ENCvigenere(entrada, chave):
    entrada = entrada.upper()
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
