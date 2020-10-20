import string
string.ascii_letters
import itertools
valor="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for L in range(1, 4):
    for subset in itertools.combinations(valor, L):
        print(subset)