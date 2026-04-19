import random
minimo = 0

dificultad = input("Elige la dificultad (F,M,D): ")
if dificultad == "F":
    maximo = 10
elif dificultad == "M":
    maximo = 50
elif dificultad == "D":
    maximo=100
elif dificultad not in "DMF":
    print("ERROR, NO SE ENCONTRO LA DIFICULTAD")
    maximo = 10

numero_azar = random.randint(minimo,maximo)
intentos = 0
while True:
    intento_usuario = int(input(f"introduce un numero [{minimo} - {maximo}]: "))
    intentos += 1
    if intento_usuario > numero_azar:
        print("El numero es mas pequeño que " + str(intento_usuario))
    elif intento_usuario < numero_azar:
        print("El numero es mas grande " + str(intento_usuario))
    else:
        break
print("Has acertado! El numero era " + str(numero_azar))
print(f"Has tardado {intentos} intentos")
