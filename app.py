from src.procesador import procesar_reporte

def mostrar_menu():
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN ADMINISTRATIVA")
    print("="*40)
    print("1. Procesar nuevo reporte")
    print("2. Salir")
    print("="*40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                id_adm = input("Ingrese el ID administrativo (10 dígitos): ")
                valor = float(input("Ingrese el valor del reporte: "))
                
                datos = {'id_administrativo': id_adm, 'valor': valor}
                resultado, mensaje = procesar_reporte(datos)
                
                print(f"\n[ESTADO]: {mensaje.upper()}")
            except ValueError:
                print("\n[ERROR]: El valor debe ser numérico.")
                
        elif opcion == "2":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\n[ERROR]: Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()