#Hola profe!, este es mi programa :)

class Animal:
    """Clase base para todos los animales"""

    def __init__(self, nombre):
        self.nombre = nombre
        self._edad = 0  # Atributo encapsulado (por convención con _)

    def hacer_sonido(self):
        """Método que será sobrescrito (polimorfismo)"""1
        return "Hace algún sonido"

    def cumplir_anios(self):
        """Método para incrementar la edad"""
        self._edad += 1
        return f"{self.nombre} ahora tiene {self._edad} años"


class Perro(Animal):
    """Clase derivada que hereda de Animal"""

    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Hereda el constructor
        self.raza = raza

    def hacer_sonido(self):  # Sobrescribe el método (polimorfismo)
        return "¡Guau guau!"

    def info(self):
        return f"{self.nombre} es un {self.raza} de {self._edad} años"


#Programa principal
def main():
    print("🐶 MASCOTA VIRTUAL 🐶")

    # Crear instancia
    mi_perro = Perro("Rex", "Labrador")

    # Menú interactivo
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Escuchar a la mascota")
        print("2. Celebrar cumpleaños")
        print("3. Ver info")
        print("4. Salir")

        opcion = input("Opción (1-4): ")

        if opcion == "1":
            print(mi_perro.hacer_sonido())  # Polimorfismo en acción

        elif opcion == "2":
            print(mi_perro.cumplir_anios())  # Usa atributo encapsulado _edad

        elif opcion == "3":
            print(mi_perro.info())

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()