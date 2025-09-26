import tkinter as tk
from tkinter import messagebox


class ListaTareas:
    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Lista de Tareas")
        self.ventana.geometry("400x400")

        # Crear elementos de la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Campo para escribir tareas
        self.entrada_tarea = tk.Entry(self.ventana, width=30)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.bind('<Return>', lambda event: self.añadir_tarea())  # Enter para añadir

        # Botón Añadir
        boton_añadir = tk.Button(self.ventana, text="Añadir Tarea", command=self.añadir_tarea)
        boton_añadir.pack(pady=5)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(self.ventana, width=40, height=15)
        self.lista_tareas.pack(pady=10)
        self.lista_tareas.bind('<Double-Button-1>', lambda event: self.marcar_completada())  # Doble clic

        # Frame para botones inferiores
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        # Botones de acciones
        boton_completada = tk.Button(frame_botones, text="Marcar Completada", command=self.marcar_completada)
        boton_completada.grid(row=0, column=0, padx=5)

        boton_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        boton_eliminar.grid(row=0, column=1, padx=5)

    def añadir_tarea(self):
        # Obtener texto de la entrada
        tarea = self.entrada_tarea.get().strip()

        # Verificar que no esté vacía
        if tarea:
            self.lista_tareas.insert(tk.END, tarea)  # Añadir a la lista
            self.entrada_tarea.delete(0, tk.END)  # Limpiar campo
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea primero")

    def marcar_completada(self):
        # Obtener tarea seleccionada
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            tarea = self.lista_tareas.get(indice)

            # Marcar con ✓ si no está marcada
            if not tarea.startswith("✓ "):
                self.lista_tareas.delete(indice)
                self.lista_tareas.insert(indice, "✓ " + tarea)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

    def eliminar_tarea(self):
        # Obtener tarea seleccionada
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            self.lista_tareas.delete(seleccion[0])  # Eliminar tarea
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea primero")

    def ejecutar(self):
        # Iniciar la aplicación
        self.ventana.mainloop()


# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = ListaTareas()
    app.ejecutar()

#Fin