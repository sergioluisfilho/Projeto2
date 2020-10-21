alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X", "Y", "Z",]

def ENCcesarV1(entrada, chave):
    entrada = entrada.upper()  # Qualquer string passada como parametro + uma chave inteira qualquer, retornará uma string apenas com letras de a-z não acentuadas e sem qualquer tipo de caractere
    nova_string = ""
    for c in entrada:
        interador = alfabeto.index(c)
        numero = (interador + chave) % 26
        interador = alfabeto[numero]
        nova_string += interador
    return nova_string