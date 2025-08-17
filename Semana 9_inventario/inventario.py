from producto import Producto

# Clase Inventario para manejar la lista de productos y operaciones
class Inventario:
    # Constructor que inicializa la lista de productos vacía
    def __init__(self):
        self.lista_productos = []

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        # Verificar que no exista otro producto con el mismo código
        for p in self.lista_productos:
            if p.obtener_codigo() == producto.obtener_codigo():
                print("Error: Código ya existe")
                return
        # Si el código es único, se agrega el producto
        self.lista_productos.append(producto)
        print("Producto agregado")

    # Método para eliminar un producto por su código
    def eliminar_producto(self, codigo):
        # Se crea una nueva lista excluyendo el producto con el código dado
        self.lista_productos = [p for p in self.lista_productos if p.obtener_codigo() != codigo]
        print("Producto eliminado si existía")

    # Método para actualizar la cantidad o precio de un producto
    def actualizar_producto(self, codigo, nueva_cantidad=None, nuevo_precio=None):
        for p in self.lista_productos:
            if p.obtener_codigo() == codigo:
                # Si se envía nueva cantidad, se actualiza
                if nueva_cantidad is not None:
                    p.cambiar_cantidad(nueva_cantidad)
                # Si se envía nuevo precio, se actualiza
                if nuevo_precio is not None:
                    p.cambiar_precio(nuevo_precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    # Método para buscar productos por nombre
    def buscar_productos(self, nombre):
        # Se devuelven los productos cuyo nombre contiene la cadena buscada
        encontrados = [p for p in self.lista_productos if nombre.lower() in p.obtener_nombre().lower()]
        return encontrados

    # Método para mostrar todos los productos del inventario
    def mostrar_todos(self):
        if not self.lista_productos:
            print("No hay productos en el inventario")
        for p in self.lista_productos:
            print(f"Código: {p.obtener_codigo()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")
