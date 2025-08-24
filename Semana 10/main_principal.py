from producto import Producto
from inventario import Inventario


def menu():
    inv = Inventario()  # Ahora carga automáticamente desde archivo

    while True:
        print("\n=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                p = Producto(codigo, nombre, cantidad, precio)
                inv.agregar_producto(p)
            except:
                print("Error: Datos inválidos")

        elif opcion == "2":
            codigo = input("Código a eliminar: ")
            inv.eliminar_producto(codigo)

        elif opcion == "3":
            try:
                codigo = input("Código a actualizar: ")
                cant = input("Nueva cantidad (vacío para no cambiar): ")
                prec = input("Nuevo precio (vacío para no cambiar): ")

                nueva_cant = int(cant) if cant else None
                nuevo_prec = float(prec) if prec else None

                inv.actualizar_producto(codigo, nueva_cant, nuevo_prec)
            except:
                print("Error: Datos inválidos")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            encontrados = inv.buscar_productos(nombre)
            if encontrados:
                for p in encontrados:
                    print(f"Código: {p.codigo}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
            else:
                print("No se encontraron productos")

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()