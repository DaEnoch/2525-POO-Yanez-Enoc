from producto import Producto


class Inventario:
    def __init__(self):
        self.lista_productos = []
        self.archivo = "inventario.txt"
        self.cargar_inventario()  # Cargar productos al iniciar

    def cargar_inventario(self):
        # Intentar cargar productos desde archivo
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos
                        producto = Producto(codigo, nombre, int(cantidad), float(precio))
                        self.lista_productos.append(producto)
            print("Inventario cargado desde archivo")
        except FileNotFoundError:
            # Si el archivo no existe, es normal la primera vez
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except:
            print("Error al cargar el archivo de inventario")

    def guardar_inventario(self):
        # Guardar todos los productos en el archivo
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.lista_productos:
                    linea = f"{producto.codigo},{producto.nombre},{producto.cantidad},{producto.precio}\n"
                    f.write(linea)
            return True
        except:
            print("Error al guardar en archivo")
            return False

    def agregar_producto(self, producto):
        # Verificar si el código ya existe
        for p in self.lista_productos:
            if p.codigo == producto.codigo:
                print("Error: Código ya existe")
                return False

        self.lista_productos.append(producto)
        if self.guardar_inventario():
            print("Producto agregado y guardado")
            return True
        else:
            print("Error al guardar en archivo")
            return False

    def eliminar_producto(self, codigo):
        # Buscar y eliminar producto
        for i, p in enumerate(self.lista_productos):
            if p.codigo == codigo:
                self.lista_productos.pop(i)
                if self.guardar_inventario():
                    print("Producto eliminado y guardado")
                    return True
                else:
                    print("Error al guardar en archivo")
                    return False
        print("Producto no encontrado")
        return False

    def actualizar_producto(self, codigo, nueva_cantidad=None, nuevo_precio=None):
        # Buscar y actualizar producto
        for p in self.lista_productos:
            if p.codigo == codigo:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                if self.guardar_inventario():
                    print("Producto actualizado y guardado")
                    return True
                else:
                    print("Error al guardar en archivo")
                    return False
        print("Producto no encontrado")
        return False

    def buscar_productos(self, nombre):
        # Buscar productos por nombre
        encontrados = []
        for p in self.lista_productos:
            if nombre.lower() in p.nombre.lower():
                encontrados.append(p)
        return encontrados

    def mostrar_todos(self):
        # Mostrar todos los productos
        if not self.lista_productos:
            print("No hay productos")
        for p in self.lista_productos:
            print(f"Código: {p.codigo}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")