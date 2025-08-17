# Clase Producto para representar un producto del inventario
class Producto:
    # Constructor para inicializar el producto con código, nombre, cantidad y precio
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los valores de los atributos
    def obtener_codigo(self):
        return self.codigo

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos para modificar los valores de los atributos
    def cambiar_nombre(self, nombre):
        self.nombre = nombre

    def cambiar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def cambiar_precio(self, precio):
        self.precio = precio
