import tkinter as tk
from tkinter import ttk, messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Enoc's AgendDate")
ventana.geometry("500x400")

# Título personalizado
titulo = tk.Label(ventana, text="Enoc's AgendDate", font=("Arial", 16, "bold"), fg="blue")
titulo.pack(pady=5)

# Crear TreeView para mostrar eventos
tree = ttk.Treeview(ventana, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
tree.heading('Fecha', text='Fecha')
tree.heading('Hora', text='Hora')
tree.heading('Descripción', text='Descripción')
tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Frame para los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Campo para fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5)
entry_fecha = tk.Entry(frame_entrada, width=12)
entry_fecha.grid(row=0, column=1, padx=5)

# Campo para hora
tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5)
entry_hora = tk.Entry(frame_entrada, width=8)
entry_hora.grid(row=0, column=3, padx=5)

# Campo para descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5)
entry_desc = tk.Entry(frame_entrada, width=30)
entry_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)


# Función para agregar evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    desc = entry_desc.get()

    if fecha and hora and desc:  # Verificar que todos los campos tengan datos
        tree.insert('', 'end', values=(fecha, hora, desc))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Por favor complete todos los campos")


# Función para eliminar evento
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Error", "Seleccione un evento para eliminar")


# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento, bg="lightgreen")
btn_agregar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento, bg="lightcoral")
btn_eliminar.pack(side=tk.LEFT, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit, bg="lightblue")
btn_salir.pack(side=tk.LEFT, padx=5)

# Ejecutar la aplicación
ventana.mainloop()