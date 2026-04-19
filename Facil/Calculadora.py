"""
1.- Nos pida un numero
2.- nos pida un segundo numero
3.- nos pida una operacion
"""

operaciones_posibles = ["+","-","*","/"]

numero1 = int(input("Introduce numero 1: "))
operacion = input("Introduce una operacion [+ - * /]: ")
numero2 = int(input("Introduce numero 2: "))

while operacion not in operaciones_posibles:
    operacion = input("Introduce una operacion [+ - * /]: ")
try:
    resultado = eval(f"{numero1} {operacion} {numero2}")
except ZeroDivisionError:
    resultado = "Error"
    print("Error al dividir por zero")

print(f"{numero1} {operacion} {numero2} = {resultado}")