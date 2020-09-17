alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z",]

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


