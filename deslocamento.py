alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x", "y", "z",]

def ENCcesarV1(entrada, chave):  # Qualquer string passada como parametro + uma chave inteira qualquer, retornará uma string apenas com letras de a-z não acentuadas e sem qualquer tipo de caractere
    nova_string = ""
    for c in entrada:
        interador = alfabeto.index(c)
        numero = (interador + chave) % 26
        interador = alfabeto[numero]
        nova_string += interador
    return nova_string