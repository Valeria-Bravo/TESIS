import unittest
from unittest.mock import patch, Mock
import pygame
import time
import random
import sys

class TestMemoryGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((800, 600))

    def tearDown(self):
        pygame.quit()

    @patch('sys.exit')
    def test_quit_event(self, mock_exit):
        # Mock the QUIT event
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        sys.exit.assert_called()

    @patch('time.time', Mock(return_value=0))
    def test_show_hide_tiles(self):
        import JuegoMemoria  # Reemplaza 'JuegoMemoria' con el nombre real de tu módulo
        JuegoMemoria.puede_jugar = 1
        JuegoMemoria.x1, JuegoMemoria.y1 = 0, 0
        JuegoMemoria.x2, JuegoMemoria.y2 = 1, 1
        JuegoMemoria.ultimos_segundos = 0

        time.time.return_value = JuegoMemoria.ultimos_segundos + JuegoMemoria.segundos_mostrar_pieza + 1
        JuegoMemoria.pantalla_juego = Mock()
        JuegoMemoria.pantalla_juego.fill = Mock()
        JuegoMemoria.pantalla_juego.blit = Mock()
        JuegoMemoria.ocultar_todos_los_cuadros()

        JuegoMemoria.pantalla_juego.blit.assert_called()

    def test_win_game(self):
        import JuegoMemoria  # Reemplaza 'JuegoMemoria' con el nombre real de tu módulo
        for fila in JuegoMemoria.cuadros:
            for cuadro in fila:
                cuadro.descubierto = True

        self.assertTrue(JuegoMemoria.gana())

    def test_restart_game(self):
        import JuegoMemoria  # Reemplaza 'JuegoMemoria' con el nombre real de tu módulo
        JuegoMemoria.reiniciar_juego()
        self.assertFalse(JuegoMemoria.juego_iniciado)

if __name__ == '__main__':
    unittest.main()
