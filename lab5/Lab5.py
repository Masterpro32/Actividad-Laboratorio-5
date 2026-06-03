#Diego: importación de librerías, definición de archivos y función para cargar contactos

# Importamos os para verificar si existen archivos
import os

# Importamos pickle para guardar y leer datos en archivo binario
import pickle


# Nombre del archivo de texto donde se guardarán los contactos
ARCHIVO_TEXTO = "contactos.txt"

# Nombre del archivo binario donde también se podrán guardar los contactos
ARCHIVO_BINARIO = "contactos.dat"


def cargar_contactos_txt():
    # Lista donde se almacenarán temporalmente los contactos leídos
    contactos = []

    # Verifica si el archivo de texto existe
    # Si no existe, devuelve la lista vacía
    if not os.path.exists(ARCHIVO_TEXTO):
        return contactos

    # Abre el archivo de texto en modo lectura
    with open(ARCHIVO_TEXTO, "r", encoding="utf-8") as archivo:
        # Recorre el archivo línea por línea
        for linea in archivo:
            # Elimina espacios o saltos de línea al inicio y final
            linea = linea.strip()

            # Si la línea está vacía, la salta
            if linea == "":
                continue

            # Separa los datos usando la coma como separador
            datos = linea.split(",")

            # Verifica que la línea tenga exactamente 3 datos: id, nombre y teléfono
            if len(datos) == 3:
                # Crea un diccionario con los datos del contacto
                contacto = {
                    "id": datos[0],
                    "nombre": datos[1],
                    "telefono": datos[2]
                }

                # Agrega el contacto a la lista
                contactos.append(contacto)

    # Devuelve la lista de contactos cargados desde el archivo
    return contactos




#Harol: Función de guardar y leer datos binarios además del menú
def guardar_y_leer_binario():
    print("\n--- ARCHIVO BINARIO ---")

    # Carga los contactos desde el archivo de texto
    contactos = cargar_contactos_txt()

    # Si no hay contactos, no se puede generar el archivo binario
    if len(contactos) == 0:
        print("No hay contactos para guardar en archivo binario.")
        return

    try:
        # Abre el archivo binario en modo escritura
        # wb significa write binary
        with open(ARCHIVO_BINARIO, "wb") as archivo:
            # Guarda la lista de contactos en formato binario
            pickle.dump(contactos, archivo)

        print("Contactos guardados en archivo binario correctamente.")

        # Abre el archivo binario en modo lectura
        # rb significa read binary
        with open(ARCHIVO_BINARIO, "rb") as archivo:
            # Recupera los contactos guardados en el archivo binario
            contactos_recuperados = pickle.load(archivo)

        print("\nDatos recuperados desde el archivo binario:")

        # Muestra los contactos recuperados del archivo binario
        for contacto in contactos_recuperados:
            print(f"{contacto['id']} - {contacto['nombre']} - {contacto['telefono']}")

    except (IOError, pickle.PickleError) as e:
        # Captura errores relacionados con archivos o pickle
        print(f"Error al manejar el archivo binario: {e}")


def menu():
    # Bucle principal del sistema
    # Se repite hasta que el usuario elija salir
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE CONTACTOS =====")
        print("1. Registrar contacto")
        print("2. Mostrar archivo de texto línea por línea")
        print("3. Mostrar contactos en tabla")
        print("4. Buscar contacto")
        print("5. Contar contactos")
        print("6. Guardar y leer archivo binario")
        print("7. Salir")

        # Solicita la opción
        opcion = input("Seleccione una opción: ")

        # Ejecuta una función según la opción elegida
        if opcion == "1":
            registrar_contacto()
        elif opcion == "2":
            mostrar_archivo_linea_por_linea()
        elif opcion == "3":
            mostrar_contactos_ordenados()
        elif opcion == "4":
            buscar_contacto()
        elif opcion == "5":
            contar_contactos()
        elif opcion == "6":
            guardar_y_leer_binario()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Inicia el programa llamando al menú principal
menu()
