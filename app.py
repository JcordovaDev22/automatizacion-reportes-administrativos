import sys
from src.procesador import procesar_reporte

def ejecutar_menu():
    """Lógica separada del menú para permitir pruebas"""
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN ADMINISTRATIVA")
    print("="*40)
    print("1. Procesar nuevo reporte")
    print("2. Salir")
    print("="*40)
    
    opcion = input("Seleccione una opción: ")
    return opcion

def procesar_logica():
    """Función independiente para procesar reportes"""
    try:
        id_adm = input("Ingrese el ID administrativo (10 dígitos): ")
        valor = float(input("Ingrese el valor del reporte: "))
        
        datos = {'id_administrativo': id_adm, 'valor': valor}
        resultado, mensaje = procesar_reporte(datos)
        
        print(f"\n[ESTADO]: {mensaje.upper()}")
        return True
    except ValueError:
        print("\n[ERROR]: El valor debe ser numérico.")
        return False

def main():
    # Detectar si estamos corriendo pruebas (modo CI)
    if len(sys.argv) > 1 and sys.argv[1] == "--no-input":
        print("Ejecutando en modo de prueba automatizado.")
        return

    while True:
        opcion = ejecutar_menu()
        
        if opcion == "1":
            procesar_logica()
        elif opcion == "2":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\n[ERROR]: Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()