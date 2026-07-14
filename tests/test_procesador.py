from src.procesador import procesar_reporte

def test_procesar_reporte_valido():
    datos = {'id_administrativo': '1234567890', 'valor': 100}
    valido, mensaje = procesar_reporte(datos)
    assert valido == True
    assert mensaje == "Reporte procesado"

def test_procesar_reporte_id_invalido():
    datos = {'id_administrativo': '123', 'valor': 100}
    valido, mensaje = procesar_reporte(datos)
    assert valido == False
    assert mensaje == "ID inválido"

def test_procesar_reporte_valor_negativo():
    datos = {'id_administrativo': '1234567890', 'valor': -50}
    valido, mensaje = procesar_reporte(datos)
    assert valido == False
    assert mensaje == "Valor negativo no permitido"