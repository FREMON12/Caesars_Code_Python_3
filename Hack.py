import string
import random
key = random.randrange(26)
en = open('en.txt', 'r')
T1 = en.read()
fr = open('fr.txt', 'r')
T2 = fr.read()

ENGLISH = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047, 0.0357,
           0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116, 0.0169, 0.0028,
           0.0164, 0.0004)
FRENCH = (0.0840, 0.0106, 0.0303, 0.0418, 0.1726, 0.0112, 0.0127, 0.0092, 0.0734, 0.0031, 0.0005, 0.0601,
          0.0296, 0.0713, 0.0526, 0.0301, 0.0099, 0.0655, 0.0808, 0.0707, 0.0574, 0.0132, 0.0004, 0.0045,
          0.0030, 0.0012)
EN_FR = (ENGLISH, FRENCH)


def Encryption(message, key):
    encripted = ''
    ASC_A = ord('a')
    for letter in message.lower():
        if 'a' <= letter <= 'z':
            encripted += chr(ASC_A + (ord(letter) - ASC_A + key) % 26)
        else:
            encripted += letter
    return encripted


def delta(source, dest):
    N = 0.0
    for f1, f2 in zip(source, dest):
        N += abs(f1 - f2)
    return N


def frequency(s):
    alphabet = dict([(c, 0) for c in string.ascii_lowercase])
    N = 0.0
    for c in s:
        if 'a' <= c <= 'z':
            N += 1
            alphabet[c] += 1
    L = alphabet.items()
    L1 = sorted(L)
    return [f / N for (l, f) in L1]


def Descryption(message):
    deltamin = 1000
    bestrot = 0
    freq = frequency(message)
    for key in range(26):
        d = min([delta(freq[key:] + freq[:key], x) for x in EN_FR])
        if d < deltamin:
            deltamin = d
            bestrot = key
    return Encryption(message, -bestrot)


def hack_en():
    for text in (T1, T2):
        X = Encryption(text, key)
        X1 = Descryption(X)
        return X1


def hack_fr():
    for text in (T1, T2):
        X = Encryption(text, key)
        X1 = Descryption(X)
    return X1


def encript_hack_en():
    for text in (T1, T2):
        X = Encryption(text, key)
        return X


def encript_hack_fr():
    for text in (T1, T2):
        X = Encryption(text, key)
    return X
