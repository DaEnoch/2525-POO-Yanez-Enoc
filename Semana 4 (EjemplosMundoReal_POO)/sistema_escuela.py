class Alumno:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = []  # Lista de cursos

    def inscribir_curso(self, curso):
        """Agrega un curso a la lista del alumno si no está inscrito."""
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            print(f"{self.nombre} se inscribió en {curso}.")
        else:
            print(f"{self.nombre} ya está en {curso}.")

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor

    def __str__(self):
        # Muestra el nombre del curso y su profesor
        return f"{self.nombre} (Prof: {self.profesor})"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear cursos
    mate = Curso("Matemáticas", "Prof. García")
    prog = Curso("Programación", "Prof. López")

    # Alumno se inscribe
    alumno = Alumno("Carlos", 15)
    alumno.inscribir_curso(mate)
    alumno.inscribir_curso(prog)

#:)