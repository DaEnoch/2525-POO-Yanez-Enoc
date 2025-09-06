# main.py
# Pruebas del sistema - Versión simplificada

from biblioteca import Libro, Usuario, Biblioteca

# Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros
print("=== AGREGANDO LIBROS ===")
libro1 = Libro("Python Básico", "Juan Pérez", "Programación", "001")
libro2 = Libro("POO en Python", "Ana López", "Programación", "002")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
print("\n=== REGISTRANDO USUARIOS ===")
usuario1 = Usuario("Carlos", "U001")
biblioteca.registrar_usuario(usuario1)

# Prestar un libro
print("\n=== PRESTANDO LIBRO ===")
biblioteca.prestar_libro("U001", "001")

# Buscar libros
print("\n=== BUSCANDO LIBROS ===")
resultados = biblioteca.buscar_libro("Python")
for titulo, isbn, estado in resultados:
    print(f"- {titulo} (ISBN: {isbn}) - {estado}")

# Listar préstamos
print("\n=== LIBROS PRESTADOS ===")
prestamos = biblioteca.listar_prestamos("U001")
for libro in prestamos:
    print(f"- {libro}")

# Devolver libro
print("\n=== DEVOLVIENDO LIBRO ===")
biblioteca.devolver_libro("U001", "001")

# Dar de baja usuario
print("\n=== DANDO DE BAJA USUARIO ===")
biblioteca.dar_baja_usuario("U001")
