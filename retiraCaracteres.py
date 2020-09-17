alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z",]

def retiraCaracteres(entrada):
    entrada = entrada.lower()
    nova_entrada = ""
    for c in entrada:
        if c in alfabeto:
            nova_entrada += c
        else:
            if c == "à" or c == "á" or c == "ã":
                nova_entrada += "a"
            elif c == "é" or c == "ê":
                nova_entrada += "e"
            elif c == "ç":
                nova_entrada += "c"
            elif c == "í":
                nova_entrada += "i"
            elif c == "ó" or c == "ô" or c == "õ":
                nova_entrada += "o"
    return nova_entrada