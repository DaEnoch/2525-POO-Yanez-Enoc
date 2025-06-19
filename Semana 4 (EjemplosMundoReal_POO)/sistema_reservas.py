class Habitacion:
    def __init__(self, numero, capacidad, precio):
        # Atributos de la habitación
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.reservada = False  # Estado inicial

    def reservar(self):
        """Cambia el estado de la habitación a 'reservada'."""
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def __str__(self):
        # Muestra info de la habitación
        estado = "Reservada" if self.reservada else "Disponible"
        return f"Habitación {self.numero} - ${self.precio}/noche ({estado})"

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []  # Lista de objetos Habitacion

    def agregar_habitacion(self, habitacion):
        """Añade una habitación al hotel."""
        self.habitaciones.append(habitacion)

# Ejemplo de uso
if __name__ == "__main__":
    hotel = Hotel("Hotel Python")
    hab1 = Habitacion(101, 2, 100)
    hab2 = Habitacion(102, 4, 200)

    hotel.agregar_habitacion(hab1)
    hotel.agregar_habitacion(hab2)

    hab1.reservar()  # Reservar habitación 101

#:)