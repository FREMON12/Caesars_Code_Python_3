# import string


# Шифровка
def Encryption(key, message, alphabet):
    encrypted = ''
    for letter in message:
        letter = letter.lower()
        if letter not in alphabet:
            encrypted += letter
        elif letter.isalpha():
            encrypted += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        elif ' ' or '/t' or '/n' in letter:
            encrypted += letter
        elif letter.isnumeric():
            encrypted += letter
    return encrypted


# Расшифровка
def Descryption(key, message, alphabet):
    descryptin = ''
    for letter in message:
        letter = letter.lower()
        if letter not in alphabet:
            descryptin += letter
        elif letter.isalpha():
            descryptin += alphabet[(alphabet.index(letter) - key) % len(alphabet)]
        elif ' ' or '/t' or '/n' in letter:
            descryptin += letter
        elif letter.isnumeric():
            descryptin += letter
    return descryptin
