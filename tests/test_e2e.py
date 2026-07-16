import unittest
from unittest.mock import patch
from app import procesar_logica

class TestE2E(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1234567890', '150.50'])
    def test_flujo_completo_procesar_reporte(self, mock_input):
        """
        Simula el flujo completo del usuario: 
        1. Ingresa ID administrativo
        2. Ingresa valor
        3. Verifica que la lógica se ejecuta sin errores
        """
        resultado = procesar_logica()
        self.assertTrue(resultado, "El flujo de procesamiento de reporte debería devolver True")

    @patch('builtins.input', side_effect=['ID_INVALIDO', 'no_es_numero'])
    def test_flujo_error_valores(self, mock_input):
        """
        Simula un flujo de error donde el usuario ingresa valores incorrectos
        """
        resultado = procesar_logica()
        self.assertFalse(resultado, "Debería fallar al procesar datos no numéricos")

if __name__ == '__main__':
    unittest.main()