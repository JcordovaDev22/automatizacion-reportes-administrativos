def procesar_reporte(datos):
    """
    Transforma datos administrativos: 
    Valida los 10 dígitos del ID, pero también asegura que el valor sea positivo.
    """
    if len(str(datos.get('id_administrativo'))) != 10:
        return False, "ID inválido"
    if datos.get('valor', 0) < 0:
        return False, "Valor negativo no permitido"
    return True, "Reporte procesado"