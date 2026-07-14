import pytest
from src.procesador import procesar_reporte

# Simulamos una base de datos simple en memoria para esta prueba
db_reportes = []

def registrar_y_validar(datos):
    """Función auxiliar que integra lógica de validación y almacenamiento."""
    valido, mensaje = procesar_reporte(datos)
    if valido:
        db_reportes.append(datos)
    return valido, mensaje

def test_integracion_flujo_completo():
    """Verifica que el registro y la persistencia en memoria funcionen juntos."""
    # 1. Intentar registrar un reporte válido
    reporte = {'id_administrativo': '1234567890', 'valor': 250}
    valido, mensaje = registrar_y_validar(reporte)
    
    assert valido == True
    assert len(db_reportes) == 1
    assert db_reportes[0]['id_administrativo'] == '1234567890'

    # 2. Intentar registrar un reporte inválido (no debe guardarse)
    reporte_invalido = {'id_administrativo': '123', 'valor': 100}
    valido, mensaje = registrar_y_validar(reporte_invalido)
    
    assert valido == False
    assert len(db_reportes) == 1  # La lista no debe haber crecido