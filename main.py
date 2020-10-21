from retiraCaracteres import retiraCaracteres

from deslocamento import ENCcesarV1
from quebraDescolamento import Findkey
from chaveAleatoria import geraChave

from vigenere import ENCvigenere
from generateVigenere import chaveVig

from bifid import *
from wordGenerator import generatePassword

import random
import time

baseDeDados = generatePassword(1, 8) #UMA PALAVRA DE ATÉ 8 LETRAS
print(baseDeDados)

#vigenere ============================================
print("""

ANALISANDO CIFRA DE VIGENERE

""")
chaves = chaveVig(5) #  Quantidade de letras de uma chave


chave = chaves[random.randint(0,len(chaves))]
chave = ''.join(map(str, chave))
print('A chave e: ', chave)
time.sleep(3)


for c in baseDeDados:
    cifrado = ENCvigenere(c, chave)
    print('cifrado: ', cifrado)
    for i in chaves:
        interador = ''.join(map(str, i))
        if interador == chave:
            print('chave encontrada: ', interador)
            break

    time.sleep(5)
    print('    ')



# BIFID ===================================================
bifid = Bifid()

print("""

ANALISANDO CIFRA DE BIFID

""")

time.sleep(2)

for c in baseDeDados:
    print('A palavra e: ', c)
    time.sleep(1)
    alpha = generateAlphabets()
    alpha = alpha.upper()
    print('a chave e: ', alpha)
    time.sleep(1)
    cifrado = bifid.encrypt(c, alpha)
    print('cifrada com a chave fica: ', cifrado)
    time.sleep(1)

   

    while True == True:
        actualAlpha = generateAlphabets().upper()
        print(actualAlpha)
        if actualAlpha == alpha:
            print('chave encontrada :', actualAlpha)
            break
    
    



        
