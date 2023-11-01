import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from menu import main_menu
from db_connection import conectar_bd, obtener_usuario_id, obtener_tipo_usuario  # Importa las funciones necesarias
import Perfiles 
import subprocess

fuente = ("Arial", 14)

def registrar_usuario():
    global usuario,nombre_entry, apellido_entry, clave_entry, email_entry, dni_entry, direccion_entry, usuario_entry, tipo_var

    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    clave = clave_entry.get()
    email = email_entry.get()
    dni = dni_entry.get()
    direccion = direccion_entry.get()
    usuario = usuario_entry.get()
    tipo_nombre = tipo_var.get()

    connection = conectar_bd()  # Conecta a la base de datos

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT tipo_id FROM tipos_de_usuarios WHERE nombre_tipo = %s", (tipo_nombre,))
        tipo_id = cursor.fetchone()

        if tipo_id:
            try:
                cursor.execute("INSERT INTO usuarios (tipo_id, nombre, apellido, clave, email, dni, direccion, usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                               (tipo_id[0], nombre, apellido, clave, email, dni, direccion, usuario))
                connection.commit()
                messagebox.showinfo("Registro Exitoso", "Usuario registrado con éxito.")
            except Exception as err:
                messagebox.showerror("Error", f"No se pudo registrar el usuario: {err}")
            finally:
                cursor.close()
                connection.close()
        else:
            messagebox.showerror("Error", "Tipo de usuario no válido.")
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")

# Función para obtener los nombres de tipo de usuarios desde la base de datos
def obtener_nombres_tipo_usuarios():
    connection = conectar_bd()  # Conecta a la base de datos

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT nombre_tipo FROM tipos_de_usuarios")
        tipos = cursor.fetchall()
        nombres_tipos = [tipo[0] for tipo in tipos]
        cursor.close()
        connection.close()
        return nombres_tipos
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return []



# Función para iniciar sesión
def iniciar_sesion():
    usuario = usuario_login_entry.get()
    clave = clave_login_entry.get()

    connection = conectar_bd()  # Conecta a la base de datos

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT usuario_id, tipo_id FROM usuarios WHERE usuario = %s AND clave = %s", (usuario, clave))
        result = cursor.fetchone()

        if result:
            usuario_id, tipo_id = result
            tipo_usuario = obtener_tipo_usuario(tipo_id)  # Utiliza una función para obtener el tipo de usuario

            if tipo_usuario == "Paciente":
                messagebox.showinfo("Inicio de Sesión Exitoso", f"Bienvenido, Paciente. Usuario ID: {usuario_id}")
                ventana_principal.destroy()
                main_menu(usuario)  # Llama a la función main_menu para pacientes
            elif tipo_usuario == "Terapeuta":
                ventana_principal.destroy()
                Perfiles.main()
            else:
                messagebox.showerror("Error", "Tipo de usuario no válido.")
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos.")
        
        cursor.close()
        connection.close()
    else:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")


ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Registro e Inicio de Sesión")
ventana_principal.geometry("500x500")
ventana_principal.configure(bg="pink")
imagen_fondo = Image.open("D:/Hector/2023/Valeria/juego/Proyecto TEA Actual/Imagenes/fondo2.jpg")
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crea un label y establece la imagen de fondo
fondo_label = tk.Label(ventana_principal, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Etiqueta de bienvenida en la ventana principal
bienvenida_label = tk.Label(ventana_principal, text="¡Bienvenido!", font=("Arial", 16, "bold"))

registro_login_button = tk.Button(ventana_principal, text="Registrarse o Iniciar Sesión", font=("Arial", 16, "bold"), command=lambda: ventana_registro_login(), bg="lightblue")
registro_login_button.pack(pady=100)

def ventana_registro_login():
    ventana_principal.withdraw()
    ventana_registro_login = tk.Toplevel()
    ventana_registro_login.title("Registro e Inicio de Sesión")
    ventana_registro_login.geometry("500x500")
    ventana_registro_login.configure(bg="pink")
    fondo_label4 = tk.Label(ventana_registro_login, image=fondo)
    fondo_label4.place(x=0, y=0, relwidth=1, relheight=1)

    seleccion_label = tk.Label(ventana_registro_login, text="Elija una opción:", font=fuente, bg="white")
    seleccion_label.pack(pady=10)

    registro_button = tk.Button(ventana_registro_login, text="Registrarse", font=("Arial", 16, "bold"), command=lambda: ventana_registro(ventana_registro_login), bg="lightblue")
    inicio_sesion_button = tk.Button(ventana_registro_login, text="Iniciar Sesión", font=("Arial", 16, "bold"), command=lambda: ventana_inicio_sesion(ventana_registro_login), bg="lightblue")

    registro_button.pack(pady=5)
    inicio_sesion_button.pack(pady=5)

def ventana_registro(ventana_anterior):
    ventana_anterior.withdraw()
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("500x500")
    fondo_label2 = tk.Label(ventana_registro, image=fondo)
    fondo_label2.place(x=0, y=0, relwidth=1, relheight=1)

    nombre_label = tk.Label(ventana_registro, text="Nombre:", font=("Arial", 14, "bold"), bg="white")
    apellido_label = tk.Label(ventana_registro, text="Apellido:", font=("Arial", 14, "bold"), bg="white")
    clave_label = tk.Label(ventana_registro, text="Clave:", font=("Arial", 14, "bold"), bg="pink")
    email_label = tk.Label(ventana_registro, text="Email:", font=("Arial", 14, "bold"), bg="white")
    dni_label = tk.Label(ventana_registro, text="DNI:", font=("Arial", 14, "bold"), bg="white")
    direccion_label = tk.Label(ventana_registro, text="Dirección:", font=("Arial", 14, "bold"), bg="white")
    usuario_label = tk.Label(ventana_registro, text="Usuario:", font=("Arial", 14, "bold"), bg="white")

    nombre_label.grid(row=0, column=0, padx=10, pady=5)
    apellido_label.grid(row=1, column=0, padx=10, pady=5)
    clave_label.grid(row=2, column=0, padx=10, pady=5)
    email_label.grid(row=3, column=0, padx=10, pady=5)
    dni_label.grid(row=4, column=0, padx=10, pady=5)
    direccion_label.grid(row=5, column=0, padx=10, pady=5)
    usuario_label.grid(row=6, column=0, padx=10, pady=5)

    global nombre_entry, apellido_entry, clave_entry, email_entry, dni_entry, direccion_entry, usuario_entry, tipo_var
    nombre_entry = tk.Entry(ventana_registro)
    apellido_entry = tk.Entry(ventana_registro)
    clave_entry = tk.Entry(ventana_registro, show="*")
    email_entry = tk.Entry(ventana_registro)
    dni_entry = tk.Entry(ventana_registro)
    direccion_entry = tk.Entry(ventana_registro)
    usuario_entry = tk.Entry(ventana_registro)
    tipo_var = tk.StringVar(ventana_registro)

    nombres_tipos = obtener_nombres_tipo_usuarios()

    tipo_dropdown = tk.OptionMenu(ventana_registro, tipo_var, *nombres_tipos)

    nombre_entry.grid(row=0, column=1, padx=10, pady=5)
    apellido_entry.grid(row=1, column=1, padx=10, pady=5)
    clave_entry.grid(row=2, column=1, padx=10, pady=5)
    email_entry.grid(row=3, column=1, padx=10, pady=5)
    dni_entry.grid(row=4, column=1, padx=10, pady=5)
    direccion_entry.grid(row=5, column=1, padx=10, pady=5)
    usuario_entry.grid(row=6, column=1, padx=10, pady=5)
    tipo_dropdown.grid(row=7, column=1, padx=10, pady=5)

    registrar_button = tk.Button(ventana_registro, text="Registrar", font=("Arial", 14, "bold"), command=lambda: registrar_usuario(), bg="lightgreen", fg="black", relief="raised")
    registrar_button.grid(row=8, columnspan=2, pady=10)

    def volver_a_registro_login():
        ventana_registro.withdraw()
        ventana_anterior.deiconify()

    volver_button = tk.Button(ventana_registro, text="Volver", font=("Arial", 14, "bold"), command=lambda: volver_a_registro_login(), bg="lightgreen", fg="black", relief="raised")
    volver_button.grid(row=9, columnspan=2, pady=10)

def ventana_inicio_sesion(ventana_anterior):
    ventana_anterior.withdraw()
    ventana_inicio_sesion = tk.Toplevel()
    ventana_inicio_sesion.title("Inicio de Sesión")
    ventana_inicio_sesion.geometry("500x500")
    fondo_label3 = tk.Label(ventana_inicio_sesion, image=fondo)
    fondo_label3.place(x=0, y=0, relwidth=1, relheight=1)

    usuario_label = tk.Label(ventana_inicio_sesion, text="Usuario:", font=fuente, bg="white")
    clave_label = tk.Label(ventana_inicio_sesion, text="Clave:", font=fuente, bg="white")

    usuario_label.pack(pady=10)
    global usuario_login_entry
    usuario_login_entry = tk.Entry(ventana_inicio_sesion)
    usuario_login_entry.pack(pady=5)

    clave_label.pack()
    global clave_login_entry
    clave_login_entry = tk.Entry(ventana_inicio_sesion, show="*")
    clave_login_entry.pack(pady=10)

    iniciar_sesion_button = tk.Button(ventana_inicio_sesion, text="Iniciar Sesión", font=("Arial", 14, "bold"), command=lambda: iniciar_sesion(), bg="lightgreen", fg="black", relief="raised")
    iniciar_sesion_button.pack(pady=10)

def obtener_usuario():
    return usuario
ventana_principal.mainloop()
