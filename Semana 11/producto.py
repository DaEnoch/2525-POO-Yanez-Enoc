# Clase Producto: representa un producto del inventario
class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los valores
    def obtener_codigo(self):
        return self.codigo

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos para modificar los valores
    def cambiar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def cambiar_precio(self, precio):
        self.precio = precio
