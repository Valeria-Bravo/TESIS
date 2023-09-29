import tkinter as tk
from tkinter import messagebox
import random

# Definimos las emociones y sus respectivas imágenes
emociones = ["contento", "triste", "enfadado", "asustado"]

# Función para iniciar el juego
def iniciar_juego():
    global puntaje
    global emociones_por_colocar
    
    puntaje = 0
    emociones_por_colocar = list(emociones)
    
    # Seleccionar 10 imágenes al azar
    random.shuffle(imagenes)
    imagenes_mostrar = imagenes[:5]
    
    # Mostrar las imágenes en los botones
    for i in range(5):
        boton = botones[i]
        boton.config(image=imagenes_mostrar[i], height=100, width=100)  # Ajustar tamaño
        if emociones_por_colocar:
            boton.emocion_correcta = emociones_por_colocar.pop()
    
    etiqueta_puntaje.config(text=f"Puntaje: {puntaje}")

# Función para verificar si la imagen está en la emoción correcta
def verificar_emocion(imagen, emocion):
    global puntaje
    
    if imagen.emocion_correcta == emocion:
        puntaje += 1
        imagen.place_forget()
        if puntaje == 5:
            messagebox.showinfo("¡Felicitaciones!", "Has colocado todas las imágenes correctamente.")
            ventana.quit()
        etiqueta_puntaje.config(text=f"Puntaje: {puntaje}")

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Actividad de Emociones para TEA")

# Cargamos las imágenes (debes asegurarte de tener al menos 10 imágenes en la lista)
imagenes = [tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/feliz.png"), 
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/feliz2.png"), 
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/triste.png"), 
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/asustado.png"),
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/asustado2.png"),
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/enojado.png"),
            tk.PhotoImage(file="C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA/Imagenes/enojado2.png")]

# Creamos botones para las imágenes
botones = []
for i in range(5):
    boton = tk.Button(ventana, command=lambda i=i: verificar_emocion(botones[i], emociones[i]))
    botones.append(boton)
    boton.grid(row=2, column=i, padx=10, pady=10)

# Etiquetas para las emociones
etiquetas_emociones = []
for i in range(4):
    etiqueta = tk.Label(ventana, text=emociones[i], font=("Arial", 12))
    etiquetas_emociones.append(etiqueta)
    etiqueta.grid(row=0, column=i, padx=10, pady=10)

# Etiqueta para mostrar el puntaje
etiqueta_puntaje = tk.Label(ventana, text="Puntaje: 0", font=("Arial", 12))
etiqueta_puntaje.grid(row=1, column=0, columnspan=4, pady=10)

# Inicializamos el puntaje y las emociones por colocar
puntaje = 0
emociones_por_colocar = []

# Iniciamos el juego
iniciar_juego()

# Iniciamos el bucle principal
ventana.mainloop()
