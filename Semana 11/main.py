from producto import Producto
from inventario import Inventario

def menu():
    inv = Inventario()
    inv.cargar_archivo()  # intenta cargar al inicio

    while True:
        print("\n=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            p = Producto(codigo, nombre, cantidad, precio)
            inv.agregar_producto(p)

        elif opcion == "2":
            codigo = input("Código del producto a eliminar: ")
            inv.eliminar_producto(codigo)

        elif opcion == "3":
            codigo = input("Código del producto a actualizar: ")
            cant = input("Nueva cantidad (enter si no cambia): ")
            prec = input("Nuevo precio (enter si no cambia): ")
            inv.actualizar_producto(
                codigo,
                nueva_cantidad=int(cant) if cant else None,
                nuevo_precio=float(prec) if prec else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            encontrados = inv.buscar_productos(nombre)
            if encontrados:
                for p in encontrados:
                    print(f"Código: {p.obtener_codigo()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")
            else:
                print("No se encontró ningún producto con ese nombre")

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            inv.guardar_archivo()

        elif opcion == "7":
            inv.guardar_archivo()  # guardamos al salir
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    menu()
