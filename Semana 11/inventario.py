import json
from producto import Producto

# Clase Inventario: maneja todos los productos
class Inventario:
    def __init__(self):
        self.lista_productos = []

    # Agregar producto (evitar repetidos por código)
    def agregar_producto(self, producto):
        for p in self.lista_productos:
            if p.obtener_codigo() == producto.obtener_codigo():
                print("Error: código ya existe")
                return
        self.lista_productos.append(producto)
        print("Producto agregado")

    # Eliminar producto
    def eliminar_producto(self, codigo):
        self.lista_productos = [p for p in self.lista_productos if p.obtener_codigo() != codigo]
        print("🗑Producto eliminado (si existía)")

    # Actualizar cantidad o precio
    def actualizar_producto(self, codigo, nueva_cantidad=None, nuevo_precio=None):
        for p in self.lista_productos:
            if p.obtener_codigo() == codigo:
                if nueva_cantidad is not None:
                    p.cambiar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.cambiar_precio(nuevo_precio)
                print("Producto actualizado")
                return
        print("Producto no encontrado")

    # Buscar productos por nombre
    def buscar_productos(self, nombre):
        encontrados = [p for p in self.lista_productos if nombre.lower() in p.obtener_nombre().lower()]
        return encontrados

    # Mostrar todos
    def mostrar_todos(self):
        if not self.lista_productos:
            print("Inventario vacío")
        for p in self.lista_productos:
            print(f"Código: {p.obtener_codigo()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")

    # Guardar en archivo (JSON)
    def guardar_archivo(self, nombre_archivo="inventario.json"):
        datos = []
        for p in self.lista_productos:
            datos.append({
                "codigo": p.obtener_codigo(),
                "nombre": p.obtener_nombre(),
                "cantidad": p.obtener_cantidad(),
                "precio": p.obtener_precio()
            })
        with open(nombre_archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print("Inventario guardado en archivo")

    # Cargar desde archivo (JSON)
    def cargar_archivo(self, nombre_archivo="inventario.json"):
        try:
            with open(nombre_archivo, "r") as f:
                datos = json.load(f)
                self.lista_productos = [Producto(d["codigo"], d["nombre"], d["cantidad"], d["precio"]) for d in datos]
            print("Inventario cargado desde archivo")
        except FileNotFoundError:
            print("No se encontró archivo de inventario, empezando vacío")
