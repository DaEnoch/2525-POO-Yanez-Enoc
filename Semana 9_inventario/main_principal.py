from producto import Producto
from inventario import Inventario

# Función principal que muestra el menú y permite interactuar con el inventario
def menu():
    inv = Inventario()  # Crear instancia del inventario
    while True:
        # Mostrar opciones del menú
        print("\n=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        # Agregar un producto
        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            p = Producto(codigo, nombre, cantidad, precio)
            inv.agregar_producto(p)

        # Eliminar un producto por código
        elif opcion == "2":
            codigo = input("Código del producto a eliminar: ")
            inv.eliminar_producto(codigo)

        # Actualizar un producto por código
        elif opcion == "3":
            codigo = input("Código del producto a actualizar: ")
            cant = input("Nueva cantidad (dejar vacío si no cambia): ")
            prec = input("Nuevo precio (dejar vacío si no cambia): ")
            inv.actualizar_producto(
                codigo,
                nueva_cantidad=int(cant) if cant else None,
                nuevo_precio=float(prec) if prec else None
            )

        # Buscar productos por nombre
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            encontrados = inv.buscar_productos(nombre)
            if encontrados:
                for p in encontrados:
                    print(f"Código: {p.obtener_codigo()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")
            else:
                print("No se encontró ningún producto con ese nombre")

        # Mostrar todos los productos
        elif opcion == "5":
            inv.mostrar_todos()

        # Salir del programa
        elif opcion == "6":
            print("Saliendo del sistema")
            break
        else:
            print("Opción no válida, intenta de nuevo")

# Ejecutar el menú solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
