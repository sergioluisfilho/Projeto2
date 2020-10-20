from RandomWordGenerator import RandomWord


def generatePassword(numberTests, wordSize):

    baseDeDados = []

    rw = RandomWord(max_word_size= wordSize,
                constant_word_size=False)

    count = 0

    while True:
        if count == numberTests:
            return baseDeDados
            break
        else:
            palavra = rw.generate()
            palavra = palavra.upper()
            count += 1
            baseDeDados.append(palavra)

# print(generatePassword(200, 5))