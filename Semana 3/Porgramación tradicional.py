# Programa para calcular el promedio de temperatura de una semana usando programación tradicional.

def ingresar_temperaturas():

    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingresa la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temps):
#calculamos el promedio de una lista de temperaturas
    return sum(temps) / len(temps)

# COdigo del programa principal
print("🌤️  Registro Semanal de Temperaturas (Programación Tradicional)")
temperaturas_semana = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas_semana)

print(f"\n📊 El promedio de temperatura esta semana fue: {promedio:.1f}°C")

#eso es todo :)