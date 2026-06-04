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

#Victoria:

def buscar_contacto():
    print("\n--- BÚSQUEDA DE CONTACTO ---")

    # Carga los contactos desde el archivo
    contactos = cargar_contactos_txt()

    # Verifica si existen contactos registrados
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    # Solicita el nombre a buscar
    # lower() permite buscar sin importar mayúsculas o minúsculas
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()

    # Valida que el usuario no deje la búsqueda vacía
    if nombre_buscar == "":
        print("Debe ingresar un nombre para buscar.")
        return

    # Variable para saber si se encontró al menos un contacto
    encontrado = False

    # Recorre la lista de contactos
    for contacto in contactos:
        # Busca coincidencias dentro del nombre del contacto
        if nombre_buscar in contacto["nombre"].lower():
            print("\nContacto encontrado:")
            print(f"ID: {contacto['id']}")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")

            # Cambia a True porque sí encontró un resultado
            encontrado = True

    # Si no encontró nada, muestra un mensaje
    if not encontrado:
        print("No se encontró ningún contacto con ese nombre.")


def contar_contactos():
    # Carga todos los contactos guardados
    contactos = cargar_contactos_txt()

    print("\n--- CONTEO DE CONTACTOS ---")

    # Muestra la cantidad total de contactos registrados
    print(f"Cantidad total de contactos registrados: {len(contactos)}")
