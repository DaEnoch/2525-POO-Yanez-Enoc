# biblioteca.py
# Sistema de Gestión de Biblioteca Digital - Versión Simplificada

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para título y autor (no cambian)
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True  # True si está disponible, False si está prestado


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros que tiene prestados


class Biblioteca:
    def __init__(self):
        # Diccionario para libros (clave: ISBN, valor: objeto Libro)
        self.libros = {}
        # Diccionario para usuarios (clave: ID usuario, valor: objeto Usuario)
        self.usuarios = {}
        # Conjunto para IDs únicos de usuarios
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca"""
        if libro.isbn in self.libros:
            print("Error: Ya existe un libro con este ISBN")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' agregado")

    def eliminar_libro(self, isbn):
        """Elimina un libro de la biblioteca"""
        if isbn not in self.libros:
            print("Error: No existe un libro con este ISBN")
        elif not self.libros[isbn].disponible:
            print("Error: No se puede eliminar un libro prestado")
        else:
            titulo = self.libros[isbn].titulo_autor[0]
            del self.libros[isbn]
            print(f"Libro '{titulo}' eliminado")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario"""
        if usuario.id_usuario in self.ids_usuarios:
            print("Error: Ya existe un usuario con este ID")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado")

    def dar_baja_usuario(self, id_usuario):
        """Da de baja a un usuario"""
        if id_usuario not in self.usuarios:
            print("Error: No existe un usuario con este ID")
        elif len(self.usuarios[id_usuario].libros_prestados) > 0:
            print("Error: El usuario tiene libros prestados")
        else:
            nombre = self.usuarios[id_usuario].nombre
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{nombre}' dado de baja")

    def prestar_libro(self, id_usuario, isbn):
        """Presta un libro a un usuario"""
        # Verificar que existe el usuario
        if id_usuario not in self.usuarios:
            print("Error: No existe el usuario")
            return

        # Verificar que existe el libro
        if isbn not in self.libros:
            print("Error: No existe el libro")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        # Verificar que el libro está disponible
        if not libro.disponible:
            print("Error: El libro no está disponible")
            return

        # Realizar el préstamo
        libro.disponible = False
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        """Devuelve un libro prestado"""
        # Verificar que existe el usuario
        if id_usuario not in self.usuarios:
            print("Error: No existe el usuario")
            return

        # Verificar que existe el libro
        if isbn not in self.libros:
            print("Error: No existe el libro")
            return

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        # Verificar que el usuario tiene prestado este libro
        if libro not in usuario.libros_prestados:
            print("Error: Este usuario no tiene prestado este libro")
            return

        # Realizar la devolución
        libro.disponible = True
        usuario.libros_prestados.remove(libro)
        print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}")

    def buscar_libro(self, texto_busqueda):
        """Busca libros por título, autor o categoría"""
        resultados = []

        for isbn, libro in self.libros.items():
            titulo, autor = libro.titulo_autor

            # Buscar en título, autor o categoría
            if (texto_busqueda.lower() in titulo.lower() or
                    texto_busqueda.lower() in autor.lower() or
                    texto_busqueda.lower() in libro.categoria.lower()):
                estado = "Disponible" if libro.disponible else "Prestado"
                resultados.append((titulo, isbn, estado))

        return resultados

    def listar_prestamos(self, id_usuario):
        """Lista los libros prestados a un usuario"""
        if id_usuario not in self.usuarios:
            print("Error: No existe el usuario")
            return []

        prestamos = []
        for libro in self.usuarios[id_usuario].libros_prestados:
            prestamos.append(libro.titulo_autor[0])

        return prestamos
