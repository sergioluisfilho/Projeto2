import string
string.ascii_letters
import itertools

def chaveVig(keySize):
    keys = []
    valor="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for L in range(1, keySize+1):
        for subset in itertools.combinations(valor, L):
            keys.append(subset)
    return keys

chaveVig(4)