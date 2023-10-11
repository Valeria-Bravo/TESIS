import tkinter as tk
import random

# Lista de colores y formas por juego
juegos = {
    "Habilidades Sociales": {'colores': ['rosado', 'azul', 'verde'], 'formas': ['corazón', 'estrella', 'círculo']},
    "Concentración": {'colores': ['amarillo', 'naranja', 'verde'], 'formas': ['triángulo', 'rectángulo', 'cuadrado']},
    "Aprendizaje en el Aula": {'colores': ['rojo', 'azul', 'morado'], 'formas': ['libro', 'calculadora', 'pizarra']}
}

# Función para iniciar el juego seleccionado
def iniciar_juego(tipo_juego):
    global puntaje
    global juego_actual
    
    juego_actual = tipo_juego
    puntaje = 0
    
    # Cambiar colores y formas según el juego seleccionado
    colores = juegos[tipo_juego]['colores']
    formas = juegos[tipo_juego]['formas']
    
    for boton in botones:
        boton.config(state=tk.NORMAL)
        color = random.choice(colores)
        forma = random.choice(formas)
        boton.config(text=f"{color} {forma}")

    etiqueta.config(text=f"Encuentra el {color} {forma}")
    etiqueta_puntaje.config(text=f"Puntaje: {puntaje}")

# Función para verificar la selección del jugador
def verificar_seleccion(color, forma):
    global puntaje
    
    color_seleccionado = etiqueta.cget('text').split()[2]
    forma_seleccionada = etiqueta.cget('text').split()[3]
    
    if color == color_seleccionado and forma == forma_seleccionada:
        puntaje += 1
        etiqueta_puntaje.config(text=f"Puntaje: {puntaje}")
    
    color = random.choice(juegos[juego_actual]['colores'])
    forma = random.choice(juegos[juego_actual]['formas'])
    etiqueta.config(text=f"Encuentra el {color} {forma}")

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Juegos para TEA")

# Creamos un menú desplegable para seleccionar el tipo de juego
opciones = tk.StringVar(ventana)
opciones.set("Seleccionar Juego")

menu = tk.OptionMenu(ventana, opciones, *juegos.keys())
menu.pack(pady=10)

# Etiqueta para indicar qué buscar
etiqueta = tk.Label(ventana, text="Selecciona un juego", font=("Arial", 14))
etiqueta.pack(pady=10)

# Creamos botones para seleccionar colores y formas
botones = []
for _ in range(3):
    boton = tk.Button(ventana, text="", command=lambda: verificar_seleccion(boton.cget('text').split()[0], boton.cget('text').split()[1]), state=tk.DISABLED)
    botones.append(boton)
    boton.pack()

# Etiqueta para mostrar el puntaje
etiqueta_puntaje = tk.Label(ventana, text="Puntaje: 0", font=("Arial", 12))
etiqueta_puntaje.pack(pady=10)

# Botón para iniciar el juego
boton_iniciar = tk.Button(ventana, text="Iniciar Juego", command=lambda: iniciar_juego(opciones.get()))
boton_iniciar.pack(pady=10)

# Inicializamos el puntaje y el juego actual
puntaje = 0
juego_actual = ""

# Iniciamos el bucle principal
ventana.mainloop()
