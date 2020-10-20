# -*- coding: utf-8 -*-
from random import shuffle
""" Classe com metodos basicos para cifras classicas """
from randomAlphabet import generateAlphabets

class Cipher(object):
    """ Classe base para as cifras classicas """
    plain_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plain_alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
 
    def format_str(self, text):
        '''Retorna text sem espacos e em maiusculas'''
        return text.replace(' ', '').upper()
 
    def shift_alphabet(self, alphabet, shift):
        '''Retorna alphabet com deslocamento de valor shift'''
        return alphabet[shift:] + alphabet[:shift]
 
    def create_square(self, alphabet = [], key = '', alphanum = False, replace = ['J', 'I'], sequence = False):
        """ Retorna um alfabeto numa matriz de num x num
        Por padrao, retorna uma matriz formada pelo alfabeto ABCDEFGHIKLMNOPQRSTUVWXYZ
        Se key, retorna um square com key iniciando o square
        alphanum square com letras e numeros
        replace letras a serem trocadas, so funciona se for usado somente o alfabeto
        sequence se True continua a preencher o square a partir do ultimo caracter da key
        """
        square = []
        if alphabet:
            if alphanum:
                replace = ['', '']
            # num = 5
            alfabeto = alphabet
        elif alphanum:
            # num = 6
            alfabeto = self.plain_alphanum
            replace = ['', '']
        else:
            # num = 5
            alfabeto = self.plain_alphabet
        alfabeto = self.create_alphabet(key.upper(), alfabeto, replace, sequence)##
        num = 5 + len(alfabeto) % 5
        for idx in range(0, len(alfabeto), num):
            square.append(alfabeto[idx:idx + num])
        return square
 
    def create_alphabet(self, key = '', alfabeto = plain_alphabet, replace = ['', ''], sequence = False):
        """ Retorna um alfabeto com key como chave e no inicio do alfabeto """
        if key:
            key = key_repeated(key)
            if replace[0] in key:
                key = key.replace(replace[0], replace[1])
            if sequence:
                idx = alfabeto.index(key[-1])
                alfabeto = self.shift_alphabet(alfabeto, idx)
        cipher = alfabeto.replace(replace[0], '')
        for ch_key in key:
            if ch_key in cipher:
                cipher = cipher.replace(ch_key, '')
        return key + cipher
 
    def random_alphabet(self, alphanum=False):
        """ Retorna um alfabeto aleatório """
        if alphanum:
            alfabeto = list(self.create_alphabet(alfabeto=self.plain_alphanum))
        else:
            alfabeto = list(self.create_alphabet())
        shuffle(alfabeto)
        return ''.join(alfabeto)
 
    def key_repeated(self, key):
        ''' Remove caracteres repetidos da senha key '''
        temp = ''
        for ch in key.upper():
            if ch not in temp:
                temp += ch
        return temp

# -*- coding: utf-8 -*-
 
class Bifid(Cipher):
    def encrypt(self, plaintext, alphabet=None):
        lins = ''
        cols = ''
        plaintext = plaintext.upper()
        matriz = self.create_square(alphabet)
        for letra in plaintext:
            for lin in matriz:
                if letra in lin:
                    cols += str(lin.find(letra) + 1)
                    lins += str(matriz.index(lin) + 1)
        cipher_num = lins + cols
        ciphertext = ''
        for i in range(0, len(cipher_num), 2):
            ref = cipher_num[i:i + 2]
            ciphertext += matriz[int(ref[0]) - 1][int(ref[1]) - 1]
        return ciphertext
 
    def decrypt(self, texto, alphabet=None):
        num = ''
        plain = ''
        texto = texto.upper()
        matriz = self.create_square(alphabet)
        for letra in texto:
            for linha in matriz:
                if letra in linha:
                    num += str(matriz.index(linha) + 1) + str(linha.find(letra) + 1)
        linhas = num[:len(num)//2]
        colunas = num[len(num)//2:]
        for i in range(0, len(linhas)):
            plain += matriz[int(linhas[i]) - 1][int(colunas[i]) - 1]
        return plain

# bifid = Bifid()
# new_alpha = generateAlphabets()
# new_alpha = new_alpha.upper()

# cifrado = bifid.encrypt('OTREMPARTEASDEZ', new_alpha)
# print(cifrado)
# print(bifid.decrypt(cifrado, new_alpha))