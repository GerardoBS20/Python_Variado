import string
import random

def generat_password(min_lenght, numbers=True,special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers
        if special_characters:
            meet_criteria = meet_criteria and has_special
    
    return pwd

min_length = int(input("ingresa el numero de caracteres: "))
has_numbers = input("Quieres que tenga numeros? (y/n) ").lower() == "y"
has_special = input("Quieres que tenga caracteres especiales? (y/n) ").lower() == "y"
pwd = generat_password(min_length,has_numbers,has_special)
print(pwd)