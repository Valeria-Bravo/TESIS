import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from Perfiles import mostrar_lista_pacientes
import db_connection
class TestPacientesFunctions(unittest.TestCase):
    @patch('Perfiles.db_connection.obtener_lista_pacientes')
    @patch('Perfiles.db_connection.obtener_datos_paciente')
    def test_mostrar_lista_pacientes(self, mock_obtener_datos_paciente, mock_obtener_lista_pacientes):

        mock_obtener_lista_pacientes.return_value = [
            (1, 'Nombre1', 'Apellido1'),
            (2, 'Nombre2', 'Apellido2')
        ]
        mock_obtener_datos_paciente.return_value = ('1', 'Nombre', 'Apellido', '12345678', 'Dirección', 'email@example.com')
        root = tk.Tk()
        button = tk.Button(root, text="Mostrar Lista de Pacientes", command=mostrar_lista_pacientes)
        button.invoke()



if __name__ == '__main__':
    unittest.main()
