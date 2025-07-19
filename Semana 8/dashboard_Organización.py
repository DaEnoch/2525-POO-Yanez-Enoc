import os

def mostrar_menu():
    print("\nMenú Principal - dashboard_Organización")
    print("1 - Semana 2/Ejemplos de Técnicas de Programación (POO).py")
    print("2 - Semana 3/Porgramación tradicional.py")  # Nota: "Porgramación" está mal escrito pero lo mantengo
    print("3 - Semana 3/Programación orientada a objetos.py")
    print("4 - Semana 4/sistema_escuela.py")
    print("4 - Semana 4/sistema_reservas.py")  # Nota: Número de opción duplicado (4)
    print("4 - Semana 4/sistema_tienda.py")    # Nota: Número de opción duplicado (4)
    print("5 - Semana 5/calculadora_de_promedio.py")
    print("6 - Semana 6/Programaa.py")         # Nota: "Programaa" con doble 'a'
    print("7 - Semana 7/código.py")
    print("8 - Semana 8/dashboard_Organización.py")
    print("9 - Terminar programa")

# Ruta base exactamente como la tenías
ruta_base = r"C:\Users\LENOVO.USER\PycharmProjects\2525-POO-Yanez-Enoc"

#Descrpción de las carpetas por semana
scripts = {
"1": os.path.join(ruta_base, "Semana 2", "Ejemplos de Técnicas de Programación (POO).py"),
"2": os.path.join(ruta_base, "Semana 3", "Porgramación tradicional.py"),
"3": os.path.join(ruta_base, "Semana 3", "Programación orientada a objetos.py"),
"4": os.path.join(ruta_base, "Semana 4", "sistema_escuela.py"),
"5": os.path.join(ruta_base, "Semana 4", "sistema_reservas.py"),
"6": os.path.join(ruta_base, "Semana 4", "sistema_tienda.py"),
"7": os.path.join(ruta_base, "Semana 5", "calculadora_de_promedio.py"),
"8": os.path.join(ruta_base, "Semana 6", "Programaa.py"),
"9": os.path.join(ruta_base, "Semana 7", "código.py"),
"10": os.path.join(ruta_base, "Semana 8", "dashboard_Organización.py"),
}


def mostrar_codigo(ruta_script):
    print(f"\nIntentando abrir: {ruta_script}\n")
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró. Verifica que exista en esa ruta.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# Bucle principal CORREGIDO (con indentación adecuada)
while True:
    mostrar_menu()  # Muestra las opciones disponibles
    opcion = input("Seleccione una opción (1-10) o 11 para terminar: ")  # Actualizado el rango

    if opcion == "11":  # Actualizado para coincidir con la opción de salida
        break
    elif opcion in scripts:
        mostrar_codigo(scripts[opcion])
    else:
        print("Opción incorrecta. Por favor, intente nuevamente.")
