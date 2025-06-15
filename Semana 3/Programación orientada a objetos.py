# Programa usando POO
# Primero creo una clase para representar el clima semanal

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
#Pide al usuario las temperaturas de los 7 días
        for dia in range(1, 8):
            temp = float(input(f"Ingresa la temperatura del día {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
#Calcula el promedio de las temperaturas almacenadas
        return sum(self.temperaturas) / len(self.temperaturas)

# Código principal del programa de promedios
print("🌤️  Registro Semanal de Temperaturas (POO)")
semana = ClimaSemanal()  # Creamos un objeto de la clase
semana.ingresar_temperaturas()
promedio = semana.calcular_promedio()

print(f"\n📊 El promedio de temperatura esta semana fue: {promedio:.1f}°C")
