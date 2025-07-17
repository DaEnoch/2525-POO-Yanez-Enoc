#Cambios de acuerdo a mi gusto
import os


class Dashboard:
    def __init__(self):
        # Guarda la ruta donde está este archivo
        self.ruta_base = os.path.dirname(__file__)
        # Diccionario con las opciones del menú
        self.opciones = {
            '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py'
        }

    def mostrar_codigo(self, ruta_script):
        # Intenta abrir y mostrar el contenido de un archivo
        try:
            with open(ruta_script, 'r') as archivo:
                print(f"\n--- Contenido de {os.path.basename(ruta_script)} ---\n")
                print(archivo.read())
        except FileNotFoundError:
            print("Archivo no encontrado")
        except:
            print("Error al leer el archivo")

    def mostrar_menu(self):
        # Muestra el menú principal en loop
        while True:
            print("\n--- MI DASHBOARD POO ---")
            print("Opciones:")
            for key, value in self.opciones.items():
                print(f"{key} - {os.path.basename(value)}")
            print("0 - Salir")

            eleccion = input("\nTu elección: ")

            if eleccion == '0':
                break
            elif eleccion in self.opciones:
                ruta_completa = os.path.join(self.ruta_base, self.opciones[eleccion])
                self.mostrar_codigo(ruta_completa)
            else:
                print("Opción incorrecta")


#Iniciar el programa
if __name__ == "__main__":
    app = Dashboard()
    app.mostrar_menu()