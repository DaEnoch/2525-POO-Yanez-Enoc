## Hola, este programa es una calculadora de promedio de notas
#Autor: Enoc Yánez

def calcular_promedio(notas):

    total = sum(notas)
    cantidad = len(notas)
    return total / cantidad


def main():
    # Aquí van los datos del estudiante (usando diferentes tipos de datos)
    nombre_estudiante = ""  # string
    edad_estudiante = 0  # integer
    activo = True  # boolean

    print("CALCULADORA DE PROMEDIO DE NOTAS")
    print("--------------------------------")

    # Solicitar datos del estudiante
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    edad_estudiante = int(input("Ingrese la edad del estudiante: "))

    # Lista para almacenar las notas (float)
    lista_notas = []

    # Solicitar cantidad de asignaturas
    cantidad_asignaturas = int(input("¿Cuántas asignaturas desea ingresar? "))

    # Ingresar notas por asignatura
    for i in range(cantidad_asignaturas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota de la asignatura {i + 1}: "))
                if 0 <= nota <= 20:  # Validar que la nota esté entre 0 y 20
                    lista_notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20. Intente nuevamente.")
            except ValueError:
                print("Por favor ingrese un número válido.")

    # Calcular promedio
    promedio_final = calcular_promedio(lista_notas)

    # Mostrar resultados
    print("\nRESULTADOS:")
    print(f"Estudiante: {nombre_estudiante}")
    print(f"Edad: {edad_estudiante} años")
    print(f"Notas ingresadas: {lista_notas}")
    print(f"Promedio final: {promedio_final:.2f}")

    # Determinar si aprobó (promedio >= 11)
    if promedio_final >= 11:
        print("Estado: APROBADO")
    else:
        print("Estado: DESAPROBADO")


if __name__ == "__main__":
    main()