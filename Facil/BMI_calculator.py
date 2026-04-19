"""Clasificación del IMC para adultos: 
Bajo peso: Menos de 18.5.
Peso saludable: 18.5 - 24.9.
Sobrepeso: 25.0 - 29.9.
Obesidad: 30.0 o más.
    """

#altura
height = float(input("ingresa la altura en metros: "))
#peso
weight =  float(input("ingresa el peso: "))

def BMI(height,weight):
    bmi = (weight)/(height**2)

    if (bmi < 18.5):
        return "Bajo peso", bmi
    
    elif (bmi >= 18.5 and bmi < 25):
        return "Peso Saludable", bmi
    
    elif (bmi >= 25 and bmi < 30):
        return "Sobrepeso", bmi
    
    elif (bmi >= 30):
        return "Obesidad", bmi
    
quote, bmi = BMI(height,weight)
print("Tu BMI es: {} y tu tienes: {}".format(bmi,quote))