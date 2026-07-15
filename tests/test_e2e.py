import requests
import pytest
from src.procesador import procesar_reporte

def test_flujo_completo_procesamiento():
    """
    Simula el flujo completo (E2E): 
    1. Registro de un reporte válido.
    2. Validación de reglas de negocio.
    """
    # Escenario: Usuario ingresa un reporte administrativo
    reporte = {'id_administrativo': '1234567890', 'valor': 500}
    
    # Acción: El sistema procesa el reporte
    resultado, mensaje = procesar_reporte(reporte)
    
    # Verificación: El sistema debe aceptar el reporte
    assert resultado == True
    assert mensaje == "Reporte procesado"
    
    # Escenario adicional: Usuario intenta ingresar datos corruptos
    reporte_error = {'id_administrativo': '000', 'valor': -10}
    
    # Acción: Procesamiento
    resultado_error, mensaje_error = procesar_reporte(reporte_error)
    
    # Verificación: El sistema debe rechazarlo
    assert resultado_error == False
    assert mensaje_error != "Reporte procesado"