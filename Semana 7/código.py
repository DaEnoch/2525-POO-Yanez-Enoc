#Hola profe, voy a crear la clase Mascota con (__init__) y usaré el destructor (__del__)
class Mascota:
    # Constructor: Se ejecuta al crear el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicializa el atributo 'nombre'
        self.edad = edad  # Inicializa el atributo 'edad'
        print(f"¡Nueva mascota creada: {self.nombre} ({self.edad} años)!")

    # Destructor: Se ejecuta al eliminar el objeto
    def __del__(self):
        print(f"{self.nombre} se ha ido... D:")  # Mensaje de "limpieza"

    # Método adicional
    def saludar(self):
        print(f"{self.nombre} dice: ¡Guau! (o ¡Miau!)")


# Programa

if __name__ == "__main__":
    # Crear objeto (llama automáticamente a __init__)
    mi_mascota = Mascota("Firulais", 3)

    mi_mascota.saludar()

    # Eliminar objeto manualmente (llama a __del__)
    del mi_mascota
