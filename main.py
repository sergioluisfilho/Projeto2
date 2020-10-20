from retiraCaracteres import retiraCaracteres

from deslocamento import ENCcesarV1
from quebraDescolamento import Findkey
from chaveAleatoria import geraChave

from vigenere import ENCvigenere
from chaveAleatoria import geraChave

from bifid import *
from wordGenerator import generatePassword

import time

baseDeDados = generatePassword(5, 5)






bifid = Bifid()


new_alpha = generateAlphabets()
new_alpha = new_alpha.upper()

for c in baseDeDados:
    cifrado = bifid.encrypt(c, new_alpha)
    print(cifrado)
    print(bifid.decrypt(cifrado, new_alpha))
