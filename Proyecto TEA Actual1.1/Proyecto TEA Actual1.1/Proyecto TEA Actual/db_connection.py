import mysql.connector

def conectar_bd():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='seminario_Tesis',
            port=3306
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def obtener_usuario_id(usuario):
    connection = conectar_bd()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT usuario_id FROM usuarios WHERE usuario = %s", (usuario,))
            result = cursor.fetchone()
            if result:
                return result[0]
        except mysql.connector.Error as err:
            print(f"Error al realizar la consulta: {err}")
        finally:
            cursor.close()
            connection.close()
    return None

def registrar_usuario(tipo_id, nombre, apellido, clave, email, dni, direccion, usuario):
    connection = conectar_bd()
    if connection:
        try:
            cursor = connection.cursor()
            # Consulta SQL para insertar un nuevo usuario en la tabla "usuarios"
            insert_query = "INSERT INTO usuarios (tipo_id, nombre, apellido, clave, email, dni, direccion, usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data = (tipo_id, nombre, apellido, clave, email, dni, direccion, usuario)
            cursor.execute(insert_query, data)
            connection.commit()  # Confirmar la inserción en la base de datos
            return cursor.lastrowid  # Devuelve el ID del usuario recién insertado
        except mysql.connector.Error as err:
            print(f"Error al registrar el usuario: {err}")
        finally:
            cursor.close()
            connection.close()
    return None

def registrar_puntaje(usuario_id, puntaje):
    connection = conectar_bd()  # Utiliza tu función conectar_bd() para obtener una conexión a la base de datos
    if connection:
        try:
            cursor = connection.cursor()
            # Consulta SQL para insertar un nuevo puntaje en la tabla "puntajes"
            insert_query = "INSERT INTO puntajes (usuario_id, puntaje) VALUES (%s, %s)"
            data = (usuario_id, puntaje)
            cursor.execute(insert_query, data)
            connection.commit()  # Confirmar la inserción en la base de datos
            return cursor.lastrowid  # Devuelve el ID del puntaje recién insertado
        except mysql.connector.Error as err:
            print(f"Error al registrar el puntaje: {err}")
        finally:
            cursor.close()
            connection.close()
    return None

