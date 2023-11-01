import unittest
from unittest.mock import patch, MagicMock
from juego_rostros import cargar_imagen_carpeta, chequear_respuesta

class TestGameFunctions(unittest.TestCase):
    def test_cargar_imagen_carpeta(self):
        carpeta = "C:/Users/ValeriaBravo/Documents/PROYECTOS PYTHON/Proyecto TEA Actual1.1/Proyecto TEA Actual1.1/Proyecto TEA Actual/Imagenes"

        archivos = ["feliz.png","feliz2.png", "asustado.png", "asustado2.png", "triste.png", "triste2.png", "enojado,png","enojado2.png"]

        with patch('os.listdir', return_value=archivos), \
             patch('pygame.image.load') as mock_load, \
             patch('pygame.transform.scale') as mock_scale:
            
            cargar_imagen_carpeta(carpeta)

            mock_load.assert_called_once()
            mock_scale.assert_called_once()

    def test_chequear_respuesta(self):#en este caso revisamos la emocion feliz
        respuesta = "feliz" 
        carpeta_correcta = "feliz"


        with patch('builtins.print') as mock_print, patch('juego_rostros.mostrar_mensaje') as mock_mostrar_mensaje:
            resultado = chequear_respuesta(respuesta, carpeta_correcta)
            mock_print.assert_called()
            mock_mostrar_mensaje.assert_called_with("CORRECTO", 400, 300, (0, 0, 255))  
            self.assertTrue(resultado) 


if __name__ == '__main__':
    unittest.main()
