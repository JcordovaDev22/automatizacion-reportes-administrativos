import pytest
from src.almacenamiento import db, guardar_datos, obtener_datos

def test_guardar():
    # Limpiamos el estado antes de la prueba
    db.clear()
    guardar_datos("suma_1", 5)
    assert "suma_1" in db
    assert db["suma_1"] == 5

def test_obtener():
    # Limpiamos el estado antes de la prueba
    db.clear()
    guardar_datos("suma_1", 5)
    resultado = obtener_datos("suma_1")
    assert resultado == 5