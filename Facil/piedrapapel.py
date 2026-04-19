import random

movimientos = ["piedra","papel","tijeras"]



puntos_usuario = 0
puntos_ia = 0

while puntos_usuario < 3 and puntos_ia <3:

    movimientos_ia = random.choice(movimientos)
    movimiento_usuario = input("Introduce tu movimiento (piedra/papel/tijera): ")

    if movimiento_usuario.lower() not in movimientos:
        print("El movimiento no esta permitido")
        quit()
    print(f"Has Sacado {movimiento_usuario}")
    print(f"El ordenador ha sacado {movimientos_ia}")

    if movimiento_usuario.lower() == "piedra":
        if movimientos_ia == "piedra":
            print("Empate")
        elif movimientos_ia == "papel":
            print("Has perdido")
            puntos_ia += 1
        elif movimientos_ia == "tijeras":
            print("Has ganado")
            puntos_usuario += 1

    elif movimiento_usuario.lower() == "papel":
        if movimientos_ia == "papel":
            print("Empate")
        elif movimientos_ia == "tijeras":
            print("Has perdido")
            puntos_ia += 1
        elif movimientos_ia == "piedra":
            print("Has ganado")
            puntos_usuario += 1

    elif movimiento_usuario.lower() == "tijeras":
        if movimientos_ia == "tijeras":
            print("Empate")
        elif movimientos_ia == "piedra":
            print("Has perdido")
            puntos_ia += 1
        elif movimientos_ia == "papel":
            print("Has ganado")
            puntos_usuario += 1
    print(f"MARCADOR: {puntos_usuario} - {puntos_ia}")

if puntos_usuario > puntos_ia:
    print(f"Has ganado a la IA: {puntos_usuario} - {puntos_ia}")
else:
    print(f"Has perdido contra la IA: {puntos_usuario} - {puntos_ia}")