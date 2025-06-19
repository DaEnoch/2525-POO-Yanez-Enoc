class Producto:
    def __init__(self, nombre, precio, stock):
        # Atributos básicos de un producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def comprar(self, cantidad):
        """Reduce el stock si hay unidades disponibles."""
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f"Se compraron {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

    def __str__(self):
        # Representación legible del producto
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        """Añade productos al carrito si hay stock."""
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            print(f"{cantidad} {producto.nombre}(s) añadido(s) al carrito.")
        else:
            print(f"Stock insuficiente de {producto.nombre}.")

# Ejemplo de uso
if __name__ == "__main__":
    # Se Crean productos
    producto1 = Producto("Laptop", 1200, 10)
    producto2 = Producto("Mouse", 20, 50)

    # Apartado para que el cliente interactúe con la tienda
    cliente = Cliente("Ana")
    cliente.agregar_al_carrito(producto1, 2)
    cliente.agregar_al_carrito(producto2, 3)

#:)