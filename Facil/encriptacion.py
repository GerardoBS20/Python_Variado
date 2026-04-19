import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

Menu = int(input("Selecciona 1 para encriptar, 2 para desencriptar: "))

if Menu == 1:
    # encriptacion
    texto = input("Ingresa el mensaje a encriptar: ")
    cipher_text = ""

    for letter in texto:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original:  {texto}")
    print(f"Mensaje encriptado: {cipher_text}")
elif Menu == 2:
    #decriptacion
    texto_cifrado = input("Ingresa el mensaje a desencriptar: ")
    texto = ""

    for letter in texto_cifrado:
        index = key.index(letter)
        texto += chars[index]

    print(f"mensaje original: {texto}")




