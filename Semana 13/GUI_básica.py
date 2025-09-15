import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título descriptivo
ventana.geometry("400x300")  # Tamaño de la ventana

# Lista para almacenar los datos
datos = []

# Función para agregar texto a la lista
def agregar_dato():
    # Obtener el texto del campo
    texto = entrada.get()
    if texto.strip() != "":
        lista.insert(tk.END, texto)  # Agregar a la lista visual
        datos.append(texto)  # Guardar en la lista interna
        entrada.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borra todos los elementos visuales
    datos.clear()  # Limpia la lista interna

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

 #eso es todo!
 #by Enoc Yanez