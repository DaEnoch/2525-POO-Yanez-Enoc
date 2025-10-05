import tkinter as tk
from tkinter import messagebox


class GestorTareas:
    def __init__(self):
        # Crear ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("400x400")

        # Lista para almacenar las tareas
        self.tareas = []

        # Configurar interfaz
        self.configurar_interfaz()

        # Configurar atajos de teclado
        self.configurar_atajos()

    def configurar_interfaz(self):
        # Campo para nueva tarea
        self.frame_entrada = tk.Frame(self.ventana)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Nueva tarea:").pack(side=tk.LEFT)
        self.entrada_tarea = tk.Entry(self.frame_entrada, width=30)
        self.entrada_tarea.pack(side=tk.LEFT, padx=5)
        self.entrada_tarea.focus()

        # Botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack(pady=5)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar (Enter)",
                                     command=self.agregar_tarea)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_completar = tk.Button(self.frame_botones, text="Completar (C)",
                                       command=self.marcar_completada)
        self.btn_completar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar (D)",
                                      command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Lista de tareas
        self.frame_lista = tk.Frame(self.ventana)
        self.frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lista_tareas = tk.Listbox(self.frame_lista, height=15)
        self.lista_tareas.pack(fill=tk.BOTH, expand=True)

    def configurar_atajos(self):
        # Vincular teclas a funciones
        self.ventana.bind('<Return>', lambda e: self.agregar_tarea())
        self.ventana.bind('c', lambda e: self.marcar_completada())
        self.ventana.bind('d', lambda e: self.eliminar_tarea())
        self.ventana.bind('<Escape>', lambda e: self.ventana.quit())

    def agregar_tarea(self):
        # Obtener texto de la entrada
        texto = self.entrada_tarea.get().strip()

        if texto:
            # Agregar a la lista y limpiar entrada
            self.tareas.append({"texto": texto, "completada": False})
            self.actualizar_lista()
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Escribe una tarea primero")

    def marcar_completada(self):
        # Obtener índice seleccionado
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            # Cambiar estado de completada
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()

    def eliminar_tarea(self):
        # Obtener índice seleccionado
        seleccion = self.lista_tareas.curselection()

        if seleccion:
            indice = seleccion[0]
            # Eliminar tarea
            del self.tareas[indice]
            self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar y volver a llenar la lista
        self.lista_tareas.delete(0, tk.END)

        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                # Marcar tareas completadas
                texto = "✓ " + texto
                self.lista_tareas.insert(tk.END, texto)
                self.lista_tareas.itemconfig(tk.END, {'fg': 'green'})
            else:
                # Tareas pendientes en negro
                self.lista_tareas.insert(tk.END, texto)
                self.lista_tareas.itemconfig(tk.END, {'fg': 'black'})

    def ejecutar(self):
        # Iniciar aplicación
        self.ventana.mainloop()


# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = GestorTareas()
    app.ejecutar()

#by Enoc Yanez