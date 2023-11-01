import tkinter as tk
from tkinter import messagebox
import db_connection
#MUESTRA LA LISTA DE TERAPEUTAS
def mostrar_lista_pacientes():
    pacientes = db_connection.obtener_lista_pacientes()

    def mostrar_detalles_paciente(usuario_id):
        datos_paciente = db_connection.obtener_datos_paciente(usuario_id)

        if datos_paciente:
            lista_pacientes.destroy()  
            detalles_paciente = tk.Tk()
            detalles_paciente.title("Detalles del Paciente")

    
            nombre, apellido, dni, direccion, email = datos_paciente[2:7]
            label = tk.Label(detalles_paciente, text=f"Nombre: {nombre} {apellido}")
            label.pack()
            label = tk.Label(detalles_paciente, text=f"DNI: {dni}")
            label.pack()
            label = tk.Label(detalles_paciente, text=f"Dirección: {direccion}")
            label.pack()
            label = tk.Label(detalles_paciente, text=f"Email: {email}")
            label.pack()

    lista_pacientes = tk.Tk()
    lista_pacientes.title("Lista de Pacientes")

    for paciente in pacientes:
        usuario_id, nombre, apellido = paciente
        label = tk.Label(lista_pacientes, text=f"{nombre} {apellido}")
        label.pack()
        button = tk.Button(lista_pacientes, text="Ver detalles", command=lambda id=usuario_id: mostrar_detalles_paciente(id))
        button.pack()

def main():
    root = tk.Tk()
    root.title("Sistema de Pacientes")

    button = tk.Button(root, text="Mostrar Lista de Pacientes", command=mostrar_lista_pacientes)
    button.pack()

    root.mainloop()
