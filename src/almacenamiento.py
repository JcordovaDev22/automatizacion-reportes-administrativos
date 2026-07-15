db = {}

def guardar_datos(key, value):
    db[key] = value

def obtener_datos(key):
    return db.get(key)