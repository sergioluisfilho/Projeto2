from deslocamento import ENCcesarV1
from retiraCaracteres import retiraCaracteres
from quebraDescolamento import Findkey

def main():
    entrada = int(input("""

    Programa de testes de algoritmos criptográficos
        Insira:

            1- Para Analisar Cifra de Deslocamento
            2- Para Analisar Cifra de Vigenere    : """))

    if entrada == 1:
        texto = input(
            """
        
        Cifra de Deslocamento foi selecionada

        Insira o texto a ser criptografado: """)
        chave = int(
            input(
                """
        
        Insira a chave (utilize apenas números inteiros): """))

        texto = retiraCaracteres(texto)
        texto_cifrado = ENCcesarV1(texto, chave)
        print("Texto cifrado: ", texto_cifrado)

        descobrir_chave = input(
            "Pressione qualquer tecla para descobrir a chave utilizada"
        )

        key = Findkey(texto_cifrado, texto)

        print("A chave de criptografia é: ", key)

    elif entrada == 2:
        print("vigenere")
    else:
        print("insira um comando válido")
main()