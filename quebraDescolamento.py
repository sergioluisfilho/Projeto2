alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z",]

def DECcesarv1(entrada, chave):
    nova_string = ""
    for c in entrada:
        interador = alfabeto.index(c)
        numero = (interador - chave) % 26
        interador = alfabeto[numero]
        nova_string += interador
    return nova_string

def Findkey(texto_cifrado, texto):
    k = 1
    while k <= 26:
        score = DECcesarv1(texto_cifrado, k)
        if score == texto:
            return k
        else:
            k +=1


