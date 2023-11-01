import unittest
import mysql.connector
from unittest.mock import MagicMock
from db_connection import (
    conectar_bd,
    obtener_usuario_id,
    registrar_usuario,
    registrar_puntaje,
    obtener_lista_pacientes,
    obtener_datos_paciente,
    obtener_tipo_usuario
)

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        self.connection = MagicMock()

    def tearDown(self):
        self.connection = None

    def test_conectar_bd(self):
        self.assertIsInstance(conectar_bd(), mysql.connector.MySQLConnection)

    def test_obtener_usuario_id(self):

        conectar_bd = MagicMock(return_value=self.connection)
        self.connection.cursor = MagicMock(return_value=self.connection)
        cursor = self.connection.cursor

        user_id = 1
        cursor.fetchone.return_value = (user_id,)
        self.assertEqual(obtener_usuario_id("Valeria"), user_id)

    def test_registrar_usuario(self):
      
        conectar_bd = MagicMock(return_value=self.connection)
        self.connection.cursor = MagicMock(return_value=self.connection)
        cursor = self.connection.cursor

        cursor.lastrowid = 12
        self.assertEqual(registrar_usuario(1, "John", "Doe", "password", "john@example.com", "12345678", "Address", "johndoe"), 12)

    def test_registrar_puntaje(self):
        conectar_bd = MagicMock(return_value=self.connection)
        self.connection.cursor = MagicMock(return_value=self.connection)
        cursor = self.connection.cursor
        cursor.lastrowid = 12
        self.assertEqual(registrar_puntaje(1, 100), 12)
if __name__ == '__main__':
    unittest.main()
