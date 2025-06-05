#Tarea de la semana 2
#Ejemplos de técnicas en POO

#1 (ABSTRACCIÓN)
class Personaje:
    def __init__(self, nombre, fuerza):
        self.nombre = nombre
        self.fuerza = fuerza

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Fuerza:", self.fuerza)

p1 = Personaje("Link", 10)
p1.mostrar_info()

#2 (ENCAPSULACIÓN)
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def mostrar_saldo(self):
        print("Saldo actual:", self.__saldo)

cuenta = Cuenta(100)
cuenta.depositar(50)
cuenta.mostrar_saldo()

#3 (HERENCIA)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print(self.nombre, "dice guau")


mi_perro = Perro("Toby")
mi_perro.hablar()

#4 (POLiMORFISMO)
class Ave:
    def hacer_sonido(self):
        print("Pío")

class Gallo:
    def hacer_sonido(self):
        print("Quiquiriquí")

def sonido(animal):
    animal.hacer_sonido()

# Se usan distintos objetos que tienen el mismo método
ave = Ave()
gallo = Gallo()

sonido(ave)
sonido(gallo)

#Eso es todo! :D
